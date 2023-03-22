class DecodedPCs:
    def __init__(self):
        self.__pcs = []
        self.__instr = []
        self.__backpressure = False

    def backpressure(self):
        return self.__backpressure

    def append(self, pc, instr):
        self.__pcs.append(pc)
        self.__instr.append(instr)

    def pop(self):
        ret_val = (self.__pcs[0], self.__instr[0])
        self.__pcs = self.__pcs[1:]
        self.__instr = self.__instr[1:]
        return ret_val

    def size(self):
        return len(self.__pcs)

    def get_json(self):
        return {"DecodedPCs": self.__pcs}
