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

    def __not_finished(self):
        return self.__cpu_state.get_pc() < len(self.__instructions)

    def __propagate(self):
        pass

    def __latch(self):
        self.__cpu_state.fetch_and_decode()
        pass

    def run(self):
        self.__parse_input_instructions()
        ans = self.__cpu_state.dump_state()

        while self.__not_finished or self.__cpu_state.busy():
            self.__propagate()
            self.__latch()
            ans += json.dumps(self.__cpu_state.dump_state())

        with open(self.__json_output, "w") as fout:
            fout.write(ans)
