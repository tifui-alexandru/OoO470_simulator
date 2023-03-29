class PhysicalRegisterFile():
    def __init__(self):
        self.__registers = [0] * 64

    def set_reg(self, register, value):
        self.__registers[register] = value

    def get_reg(self, register):
        return self.__registers[register]

    def get_json(self):
        return {"PhysicalRegisterFile": self.__registers}
