class ALU():
    def __init__(self):
        self.__instr_queue = [None, None]
        self.__forwarding_path = None

    def __exec(self, instr):
        if inst is None:
            return None


    def get_forwarding_path(self):
        return self.__forwarding_path

    def push_instr(self, new_instr):
        self.__instr_queue[1] = self.__instr_queue[0]
        self.__instr_queue[0] = new_instr

    def execute(self):
        self.__forwarding_path = self.__exec(self.__instr_queue[1])
