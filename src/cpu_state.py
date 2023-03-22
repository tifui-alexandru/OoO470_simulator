import copy

from data_structures.active_list import ActiveList
from data_structures.busy_bit_table import BusyBitTable
from data_structures.decoded_pcs import DecodedPCs
from data_structures.exception_ds import ExceptionDS
from data_structures.free_list import FreeList
from data_structures.integer_queue import IntegerQueue
from data_structures.physical_register_file import PhysicalRegisterFile
from data_structures.register_map_table import RegisterMapTable
from data_structures.pc import PC


class CPU_state():
    def __init__(self, memory):
        self.__memory = memory

        self.__pc = PC()
        self.__physical_register_file = PhysicalRegisterFile()
        self.__decoded_pcs = DecodedPCs()
        self.__exception_ds = ExceptionDS()
        self.__register_map_table = RegisterMapTable()
        self.__free_list = FreeList()
        self.__busy_bit_table = BusyBitTable()
        self.__active_list = ActiveList()
        self.__integer_queue = IntegerQueue()

        self.__data_structures = [
            self.__pc,
            self.__physical_register_file,
            self.__decoded_pcs,
            self.__exception_ds,
            self.__register_map_table,
            self.__free_list,
            self.__busy_bit_table,
            self.__active_list,
            self.__integer_queue
        ]

    def copy(self):
        return copy.deepcopy(self)

    def dump_state(self):
        ans = dict()
        for ds in self.__data_structures:
            ans |= ds.get_json()
        return ans

    def busy(self):
        return not self.__active_list.empty()

    def get_commited_instr(self):
        return self.__active_list.commited_instruction()

    def get_pc(self):
        return self.__pc.get_pc()

    def fetch_and_decode(self):
        if self.__decoded_pcs.backpressure():
            return

        for i in range(4):
            idx = self.__pc.get_pc() + i
            if idx >= len(self.__memory):
                break
            instr_arr = self.__memory[idx].split()
            instr_obj = {
                "opcode": instr_arr[0],
                "dst": instr_arr[1][:-1],
                "src1": instr_arr[2][:-1],
                "src2": instr_arr[3]
            }
            self.__decoded_pcs.append(idx, instr_obj)

    def rename_and_dispatch(self):
        buff_sz = self.__decoded_pcs.size()
        pass 
        # TODO: figure out what this stage does

    def issue(self):
        # TODO: implement this
        pass

    def execution(self):
        # TODO: implement this
        pass

    def commit(self):
        # TODO: implement this
        pass
