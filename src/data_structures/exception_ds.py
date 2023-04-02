class ExceptionDS():
    def __init__(self):
        self.__flag = False
        self.__pc = 0

    def raise_exception(self, pc):
        self.__flag = True
        self.__pc = pc

    def is_exception(self):
        return self.__flag

    def handle_exception(self):
        self.__flag = False

    def get_json(self):
        return {
            "ExceptionPC": self.__pc,
            "Exception": self.__flag
        }
