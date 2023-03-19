class DecodedPCs:
    def __init__(self):
        self.__pcs = []

    def get_json(self):
        return {"DecodedPCs": self.__pcs}
