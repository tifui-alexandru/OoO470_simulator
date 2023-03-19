class FreeList():
    def __init__(self):
        self.__max_cap = 64
        self.__list = list(range(32, 64))

    def append(self, x):
        if len(self.__list == self.__max_cap):
            return "FreeList is full"
        if x in self.__list:
            return f"Register {x} already in list"
        self.__list = [x] + self.__list
        return "OK"

    def pop(self, x):
        if len(self.__list) == 0:
            return "FreeList is empty"
        self.__list = self.__list[:-1]
        return "OK"

    def get_json(self):
        return {"FreeList": self.__list}
