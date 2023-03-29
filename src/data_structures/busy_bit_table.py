class BusyBitTable():
    def __init__(self):
        self.__table = [False] * 64

    def is_busy(self, x):
        if self.__table[x]:
            return True
        return False

    def mark_register(self, x):
        if self.__table[x]:
            raise Exception(f"Register {x} is already busy")
        self.__table[x] = True

    def unmark_register(self, x):
        self.__table[x] = False

    def get_json(self):
        return {"BusyBitTable": self.__table}
