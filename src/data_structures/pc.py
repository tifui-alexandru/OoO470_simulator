class PC():
    def __init__(self):
        self.__pc = 0

    def increment(self):
        self.__pc += 1

    def get_pc(self):
        return self.__pc

    def set_exception_pc(self):
        self.__pc = 0x10000

    def is_exception(self):
        return self.__pc == 0x10000

    def get_json(self):
        return {"PC": self.__pc}
