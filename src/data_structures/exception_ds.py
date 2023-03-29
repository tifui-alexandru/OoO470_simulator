class ExceptionDS():
    def __init__(self):
        self.__flag = False
        self.__pc = 0

    def raise_exception(self, pc):
        self.__flag = True
        self.__pc = pc

    def handle_exception(self, pc):
        self.__flag = False
        self.__pc = 0

    def get_json(self):
        return {
            "ExceptionPC": self.__pc,
            "Exception": self.__flag
        }
