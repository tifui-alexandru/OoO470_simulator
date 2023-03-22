class ExceptionDS():
    def __init__(self):
        self.__flag = "false"
        self.__pc = 0

    def raise_exception(self, pc):
        self.__flag = "true"
        self.__pc = pc

    def handle_exception(self, pc):
        self.__flag = "false"
        self.__pc = 0

    def get_json(self):
        return {
            "ExceptionPC": self.__pc,
            "Exception": self.__flag
        }
