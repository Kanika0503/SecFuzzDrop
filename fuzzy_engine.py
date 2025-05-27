import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables
cpu = ctrl.Antecedent(np.arange(0, 101, 1), 'cpu')
mem = ctrl.Antecedent(np.arange(0, 101, 1), 'mem')
latency = ctrl.Antecedent(np.arange(0, 101, 1), 'latency')
threat = ctrl.Antecedent(np.arange(0, 11, 1), 'threat')
score = ctrl.Consequent(np.arange(0, 101, 1), 'score')

# Membership functions
cpu.automf(3)
mem.automf(3)
latency.automf(3)
threat['low'] = fuzz.trimf(threat.universe, [0, 0, 5])
threat['medium'] = fuzz.trimf(threat.universe, [2, 5, 8])
threat['high'] = fuzz.trimf(threat.universe, [6, 10, 10])

score['low'] = fuzz.trimf(score.universe, [0, 0, 50])
score['medium'] = fuzz.trimf(score.universe, [25, 50, 75])
score['high'] = fuzz.trimf(score.universe, [50, 100, 100])

# Fuzzy rules
rules = [
    ctrl.Rule(cpu['good'] & mem['good'] & latency['poor'] & threat['low'], score['high']),
    ctrl.Rule(cpu['average'] | mem['average'] | latency['average'] | threat['medium'], score['medium']),
    ctrl.Rule(cpu['poor'] | mem['poor'] | latency['good'] | threat['high'], score['low']),
]

scoring_ctrl = ctrl.ControlSystem(rules)
scoring_sim = ctrl.ControlSystemSimulation(scoring_ctrl)

# Evaluation function
def evaluate_node(cpu_val, mem_val, latency_val, threat_val):
    sim = ctrl.ControlSystemSimulation(scoring_ctrl)
    sim.input['cpu'] = cpu_val
    sim.input['mem'] = mem_val
    sim.input['latency'] = latency_val
    sim.input['threat'] = threat_val
    sim.compute()
    return sim.output['score']
