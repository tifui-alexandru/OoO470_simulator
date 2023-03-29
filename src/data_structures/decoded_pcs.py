class DecodedPCs:
    def __init__(self):
        self.__pcs = []
        self.__instr = []
        self.__backpressure = False

    def apply_backpressure(self):
        self.__backpressure = True

    def backpressure(self):
        return self.__backpressure

    def append(self, pc, instr):
        self.__pcs.append(pc)
        self.__instr.append(instr)

    def get_instructions(self):
        return self.__pcs, self.__instr

    def flush(self):
        self.__pcs = []
        self.__instr = []
        self.__backpressure = False

    def get_json(self):
        return {"DecodedPCs": self.__pcs}
