import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy input variables
cpu = ctrl.Antecedent(np.arange(0, 101, 1), 'cpu')
memory = ctrl.Antecedent(np.arange(0, 101, 1), 'memory')
trust = ctrl.Antecedent(np.arange(0, 11, 1), 'trust')
latency = ctrl.Antecedent(np.arange(0, 101, 1), 'latency')
load = ctrl.Antecedent(np.arange(0, 101, 1), 'load')
threat = ctrl.Antecedent(np.arange(0, 11, 1), 'threat')

# Define fuzzy output variable
score = ctrl.Consequent(np.arange(0, 101, 1), 'score')

# Membership functions for CPU
cpu['low'] = fuzz.trimf(cpu.universe, [0, 0, 50])
cpu['medium'] = fuzz.trimf(cpu.universe, [30, 50, 70])
cpu['high'] = fuzz.trimf(cpu.universe, [50, 100, 100])

# Memory
memory['low'] = fuzz.trimf(memory.universe, [0, 0, 50])
memory['medium'] = fuzz.trimf(memory.universe, [30, 50, 70])
memory['high'] = fuzz.trimf(memory.universe, [50, 100, 100])

# Trust
trust['low'] = fuzz.trimf(trust.universe, [0, 0, 5])
trust['medium'] = fuzz.trimf(trust.universe, [2, 5, 8])
trust['high'] = fuzz.trimf(trust.universe, [5, 10, 10])

# Latency
latency['low'] = fuzz.trimf(latency.universe, [0, 0, 50])
latency['medium'] = fuzz.trimf(latency.universe, [30, 50, 70])
latency['high'] = fuzz.trimf(latency.universe, [50, 100, 100])

# Load
load['low'] = fuzz.trimf(load.universe, [0, 0, 50])
load['medium'] = fuzz.trimf(load.universe, [30, 50, 70])
load['high'] = fuzz.trimf(load.universe, [50, 100, 100])

# Threat
threat['low'] = fuzz.trimf(threat.universe, [0, 0, 5])
threat['medium'] = fuzz.trimf(threat.universe, [2, 5, 8])
threat['high'] = fuzz.trimf(threat.universe, [5, 10, 10])

# Score
score['low'] = fuzz.trimf(score.universe, [0, 0, 50])
score['medium'] = fuzz.trimf(score.universe, [30, 50, 70])
score['high'] = fuzz.trimf(score.universe, [50, 100, 100])

# Define rules
rules = [
    ctrl.Rule(cpu['low'] & memory['high'] & trust['high'] & latency['low'] & load['low'] & threat['low'], score['high']),
    ctrl.Rule(cpu['high'] | memory['low'] | threat['high'], score['low']),
    ctrl.Rule(cpu['medium'] & memory['medium'] & trust['medium'] & latency['medium'], score['medium']),
    ctrl.Rule(cpu['low'] & memory['low'] & trust['low'] & latency['high'] & load['high'] & threat['high'], score['low']),
    ctrl.Rule(trust['high'] & threat['low'], score['high']),
]

# Create control system
scoring_ctrl = ctrl.ControlSystem(rules)

def evaluate_node(cpu_val, memory_val, trust_val, latency_val, load_val, threat_val):
    sim = ctrl.ControlSystemSimulation(scoring_ctrl)
    sim.input['cpu'] = cpu_val
    sim.input['memory'] = memory_val
    sim.input['trust'] = trust_val
    sim.input['latency'] = latency_val
    sim.input['load'] = load_val
    sim.input['threat'] = threat_val
    sim.compute()
    return sim.output['score']
