class RegisterMapTable():
    def __init__(self):
        self.__table = list(range(32))

    def set_reg(self, arch_reg):
        return self.__table[arch_reg]

    def get_reg(self, arch_reg, physical_reg):
        self.__table[arch_reg] = physical_reg

    def get_json(self):
        return {"RegisterMapTable": self.__table}
