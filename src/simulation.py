import json

from cpu_state import CPU_state

class Simulation():
    def __init__(self, json_input, json_output):
        self.__json_input = json_input
        self.__json_output = json_output

    def __parse_input_instructions(self):
        with open(self.__json_input, "r") as fin:
            content = fin.read()
        self.__instructions = json.loads(content)
        self.__cpu_state = CPU_state(self.__instructions)

    def __simulate_cycle(self):
        # simulate in reverse order to avoid making a copy
        # of each data structure every time
        self.__cpu_state.commit()
        self.__cpu_state.execute()
        self.__cpu_state.issue()
        self.__cpu_state.rename_and_dispatch()
        self.__cpu_state.fetch_and_decode()

    def run(self):
        self.__parse_input_instructions()
        ans = [self.__cpu_state.dump_state()]

        while not self.__cpu_state.finished():
            self.__simulate_cycle()
            ans += [self.__cpu_state.dump_state()]
        
        with open(self.__json_output, "w") as fout:
            fout.write(json.dumps(ans, indent=2))
