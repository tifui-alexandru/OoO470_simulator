class RegisterMapTable():
    def __init__(self):
        self.__table = list(range(32))

    def get_json(self):
        return {"RegisterMapTable": self.__table}
