class PC():
    def __init__(self):
        self.__pc = 0

    def increment(self):
        self.__pc += 1

    def get_pc(self):
        return self.__pc

    def get_json(self):
        return {"PC": self.__pc}
