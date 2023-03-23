class BusyBitTable():
    def __init__(self):
        self.__table = ["false"] * 64

    def is_busy(self, x):
        if self.__table[x] == "true":
            return True
        return False

    def mark_register(self, x):
        if self.__table[x] == "true":
            raise Exception(f"Register {x} is already busy")
        self.__table[x] = "true"

    def unmark_register(self, x):
        if self.__table[x] == "false":
            raise Exception(f"Register {x} is not busy")
        self.__table[x] = "false"

    def get_json(self):
        return {"BusyBitTable": self.__table}
