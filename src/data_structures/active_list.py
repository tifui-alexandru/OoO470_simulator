class ActiveList():
    def __init__(self):
        self.__max_cap = 32
        self.__active_list = []

    def append(self, done=False, exception=False, log_dest=0,
               old_dest=0, pc=0):
        if len(self.__active_list) == self.__max_cap:
            return "The Active List is full"

        done = "true" if done else "false"
        exception = "true" if exception else "false"

        self.__active_list.append({
            "Done": done,
            "Exception": exception,
            "LogicalDestination": log_dest,
            "OldDestination": old_dest,
            "PC": pc
        })

        return "OK"
    
    def empty(self):
        return len(self.__active_list) == 0

    def commited_instruction(self):
        if self.empty():
            return None
        # TODO: actually commit the instruction
        if self.__active_list[0]["Done"] == "true":
            return self.__active_list[0]["PC"]
        else:
            return None

    def get_json(self):
        return {"ActiveList": self.__active_list}
