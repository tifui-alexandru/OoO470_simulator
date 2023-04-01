class ActiveList():
    def __init__(self):
        self.__max_cap = 32
        self.__active_list = []

    def has_enough_space(self, sz):
        return len(self.__active_list) + sz <= self.__max_cap

    def append(self, done=False, exception=False, log_dest=0,
               old_dest=0, pc=0):

        self.__active_list.append({
            "Done": done,
            "Exception": exception,
            "LogicalDestination": log_dest,
            "OldDestination": old_dest,
            "PC": pc
        })
    
    def empty(self):
        return len(self.__active_list) == 0

    def pop_if_ready(self):
        if self.empty():
            return None

        done = self.__active_list[0]["Done"]
        exception = self.__active_list[0]["Exception"]
        log_dest = self.__active_list[0]["LogicalDestination"]
        old_dest = self.__active_list[0]["OldDestination"]
        pc = self.__active_list[0]["PC"]

        if done or exception:
            if not exception:
                self.__active_list = self.__active_list[1:]
            return exception, log_dest, old_dest, pc
        else:
            return None
    
    def pop_for_exception(self):
        if self.empty():
            return None

        log_dest = self.__active_list[-1]["LogicalDestination"]
        old_dest = self.__active_list[-1]["OldDestination"]

        self.__active_list = self.__active_list[:-1]
        return log_dest, old_dest

    def mark_done(self, pc):
        for i in self.__active_list:
            if i["PC"] == pc:
                i["Done"] = True

    def mark_exception(self, pc):
        for i in self.__active_list:
            if i["PC"] == pc:
                i["Done"] = True
                i["Exception"] = True

    def get_json(self):
        return {"ActiveList": self.__active_list}
