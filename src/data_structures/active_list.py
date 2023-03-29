class ActiveList():
    def __init__(self):
        self.__max_cap = 32
        self.__active_list = []

    def has_enough_space(self, sz):
        return len(self.__active_list) + sz <= self.__max_cap

    def append(self, done=False, exception=False, log_dest=0,
               old_dest=0, pc=0):

        done = "true" if done == True else "false"
        exception = "true" if exception == True else "false"

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
        
        done, exception, log_dest, old_dest, pc = self.__active_list[0]
        done = done == "true"
        exception = exception == "false"

        if done or exception:
            self.__active_list = self.__active_list[1:]
            return exception, log_dest, old_dest, pc
        else:
            return None

    def mark_done(self, pc):
        for i in self.__active_list:
            if i["PC"] == pc:
                i["Done"] = "true"

    def mark_exception(self, pc):
        for i in self.__active_list:
            if i["PC"] == pc:
                i["Exception"] = "true"

    def get_json(self):
        return {"ActiveList": self.__active_list}
