class PhysicalRegisterFile():
    def __init__(self):
        self.__registers = [0] * 64

    def get_json(self):
        return {"PhysicalRegisterFile": self.__registers}
