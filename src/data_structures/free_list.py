class FreeList():
    def __init__(self):
        self.__list = list(range(32, 64))

    def has_enough_space(self, sz):
       return len(self.__list) >= sz 

    def append(self, x):
        if x in self.__list:
            raise Exception(f"Register {x} already in list")
        self.__list = [x] + self.__list

    def pop(self):
        ret_val = self.__list[0]
        self.__list = self.__list[1:]
        return ret_val

    def get_json(self):
        return {"FreeList": self.__list}
