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
            ob_b_tag=0,
            op_b_val=0,
            opcode=None,
            pc=0):

        op_a_ready = "true" if op_a_ready else "false"
        op_b_ready = "true" if op_b_ready else "false"

        self.__queue.append({
            "DestRegister": dest_reg,
            "OpAIsReady": op_a_ready,
            "OpARegtag": op_a_tag,
            "OpAValue": op_a_val,
            "OpBIsReady": op_b_ready,
            "OpBRegTag": op_b_tag,
            "OpBValue": op_b_val,
            "OpCode": opcode,
            "PC": pc
        })

    def get_json(self):
        return {"IntegerQueue": self.__queue}
