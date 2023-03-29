class IntegerQueue():
    def __init__(self):
        self.__max_cap = 32
        self.__queue = []

    def has_enough_space(self, sz):
        return len(self.__queue) + sz <= 32

    def append(
            self,
            dest_reg=0,
            op_a_ready=False,
            op_a_tag=0,
            op_a_val=0,
            op_b_ready=False,
            op_b_tag=0,
            op_b_val=0,
            opcode=None,
            pc=0):

        self.__queue.append({
            "DestRegister": dest_reg,
            "OpAIsReady": op_a_ready,
            "OpARegTag": op_a_tag,
            "OpAValue": op_a_val,
            "OpBIsReady": op_b_ready,
            "OpBRegTag": op_b_tag,
            "OpBValue": op_b_val,
            "OpCode": opcode,
            "PC": pc
        })

    def __is_ready(self, x):
        return x["OpAIsReady"] and x["OpBIsReady"] 

    def get_ready_instr(self):
        ready = [x for x in self.__queue if self.__is_ready(x)]
        if len(ready) > 4:
            ready = ready[:4]
        
        self.__queue = [x for x in self.__queue if x not in ready]
        return ready

    def update_state(self, reg, val):
        for i in self.__queue:
            if i["OpARegTag"] == reg:
                i["OpAReady"] = True
                i["OpAValue"] = val
            
            if i["OpBRegTag"] == reg:
                i["OpBReady"] = True
                i["OpBValue"] = val

    def get_json(self):
        return {"IntegerQueue": self.__queue}
