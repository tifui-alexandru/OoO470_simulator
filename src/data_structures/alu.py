from ctypes import c_int64, c_uint64

class ALU():
    def __init__(self):
        self.__instr_queue = [None, None]
        self.__forwarding_path = None

    def __exec(self, instr):
        if instr is None:
            return None
        
        r = instr["DestRegister"]
        a = instr["OpAValue"]
        b = instr["OpBValue"]
        op = instr["OpCode"]
        pc = instr["PC"]

        ans = 0
        exception = False
        if op == "add" or op == "addi":
            a = c_int64(a).value
            b = c_int64(b).value
            ans = a + b
            ans = c_uint64(ans).value
        elif op == "sub":
            a = c_int64(a).value
            b = c_int64(b).value
            ans = a - b
            ans = c_uint64(ans).value
        elif op == "mulu":
            a = c_uint64(a).value
            b = c_uint64(b).value
            ans = a * b
            ans = c_uint64(ans).value
        elif op == "divu":
            a = c_uint64(a).value
            b = c_uint64(b).value
            
            if b == 0:
                exception = True
            else:
                ans = a // b
                ans = c_uint64(ans).value
        elif op == "remu":
            a = c_uint64(a).value
            b = c_uint64(b).value
            
            if b == 0:
                exception = True
            else:
                ans = a % b
                ans = c_uint64(ans).value
        else:
            raise Exception("Undefined operation!")

        return r, ans, pc, exception 

    def get_forwarding_path(self):
        return self.__forwarding_path

    def push_instr(self, new_instr):
        self.__instr_queue[1] = self.__instr_queue[0]
        self.__instr_queue[0] = new_instr

    def reset(self):
        self.__instr_queue = [None, None]
        self.__forwarding_path = None

    def execute(self):
        self.__forwarding_path = self.__exec(self.__instr_queue[1])
        self.__instr_queue[1] = self.__instr_queue[0]
