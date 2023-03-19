class BusyBitTable():
    def __init__(self):
        self.__table = ["false"] * 64

    def mark_register(self, x):
        if self.__table[x] == "true":
            return f"Register {x} is already busy"
        self.__table[x] = "true"
        return "OK"

    def unmark_register(self, x):
        if self.__table[x] == "false":
            return f"Register {x} is not busy"
        self.__table[x] = "false"
        return "OK"

    def get_json(self):
        return {"BusyBitTable": self.__table}
