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
from data_structures.alu import ALU

class CPU_state():
    def __init__(self, memory):
        self.__memory = memory
        self.__alus = [ALU(), ALU(), ALU(), ALU()]

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

    def __rename_src_reg(self, x):
        if x[0] == 'x':
            return "p" + str(self.__register_map_table(int(x[1:])))
        else:
            return x

    def __rename_dst_reg(self, x):
        pr = self.__free_list.pop()
        self.__register_map_table.set_reg(int(x[1:]), pr)
        return pr

    def __get_ready_state(self, x):
        x = int(x[1:])
        if self.__busy_bit_table.is_busy(x):
            ready = False
            value = 0
            tag = x
        else:
            ready = True
            value = self.__physical_register_file.get_reg(x)
            tag = 0
        return ready, tag, value

    def rename_and_dispatch(self):
        pcs, instructions = self.__decoded_pcs.get_instructions()
        sz = len(instructions)

        if not self.__integer_queue.has_enough_space(sz) \
                or not self.__active_list.has_enough_space(sz) \
                or not self.__free_list.has_enough_space(sz):
            self.__decoded_pcs.apply_backpressure()

        renamed_instr = []
        for i in instr:
            rs1 = self.__rename_src_reg(ans["src1"])
            rs2 = self.__rename_src_reg(ans["src2"])
            rd = self.__rename_dst_reg(ans["dst"])
            obj = {
                "dst": rd,
                "src1": rs1,
                "src2": rs2
            }
            renamed_instr.append(obj)

        for idx in range(sz):
            ready_a, tag_a, val_a = self.__get_ready_state(
                renamed_instr[idx]["src1"])
            ready_b, tag_b, val_b = self.__get_ready_state(
                renamed_instr[idx]["src2"])
            self.__integer_queue.append(
                renamed_instr[idx]["dst"],
                ready_a,
                tag_a,
                val_a,
                ready_b,
                tag_b,
                val_b,
                instr[idx]["opcode"],
                pcs[idx])

            self.__active_list.append("False", "False", int(
                instr[idx]["dst"][1:]), renamed_instr[idx]["dst"], pcs[idx[])]

        for i in range(4):
            result = self.__alus[i].get_forwarding_path()
            if result is None:
                continue
            reg, val = result
            self.__physical_register_file.set_reg(reg, val)
            self.__busy_bit_table.unmark_register(reg)

    def issue(self):
        instr = self.__integer_queue.pop_ready_instr()
        for i in range(4):
            curr_instr = None
            if i < len(instr):
                curr_instr = instr[i]
            self.__alus[i].exec_cycle(curr_instr)
        # TODO:
        # select at most 4 ready instructions and send them to ALUs
        # observe changes from the fprwarding path
        pass

    def execution(self):
        # TODO: implement this
        pass

    def commit(self):
        # TODO: implement this
        pass
