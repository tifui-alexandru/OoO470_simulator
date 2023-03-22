import argparse
from simulation import Simulation

parser = argparse.ArgumentParser()
parser.add_argument("json_input")
parser.add_argument("json_output")
args = parser.parse_args()

app = Simulation(args.json_input, args.json_output)
app.run()
