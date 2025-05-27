import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def evaluate_node(cpu_val, mem_val, net_val, latency_val, disk_val, temp_val, threat_val):
    cpu = ctrl.Antecedent(np.arange(0, 101, 1), 'cpu')
    mem = ctrl.Antecedent(np.arange(0, 101, 1), 'mem')
    net = ctrl.Antecedent(np.arange(0, 101, 1), 'net')
    latency = ctrl.Antecedent(np.arange(0, 101, 1), 'latency')
    disk = ctrl.Antecedent(np.arange(0, 101, 1), 'disk')
    temp = ctrl.Antecedent(np.arange(0, 101, 1), 'temp')
    threat = ctrl.Antecedent(np.arange(0, 11, 1), 'threat')
    score = ctrl.Consequent(np.arange(0, 101, 1), 'score')

    for ant in [cpu, mem, net, latency, disk, temp]:
        ant.automf(3)

    threat['low'] = fuzz.trimf(threat.universe, [0, 0, 5])
    threat['medium'] = fuzz.trimf(threat.universe, [0, 5, 10])
    threat['high'] = fuzz.trimf(threat.universe, [5, 10, 10])

    score['poor'] = fuzz.trimf(score.universe, [0, 0, 50])
    score['average'] = fuzz.trimf(score.universe, [25, 50, 75])
    score['good'] = fuzz.trimf(score.universe, [50, 100, 100])

    rules = [
        ctrl.Rule(cpu['good'] & mem['good'] & threat['low'], score['good']),
        ctrl.Rule(cpu['average'] | mem['average'] | threat['medium'], score['average']),
        ctrl.Rule(cpu['poor'] | mem['poor'] | threat['high'], score['poor']),
    ]

    system = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(system)

    sim.input['cpu'] = cpu_val
    sim.input['mem'] = mem_val
    sim.input['net'] = net_val
    sim.input['latency'] = latency_val
    sim.input['disk'] = disk_val
    sim.input['temp'] = temp_val
    sim.input['threat'] = threat_val

    sim.compute()
    return sim.output['score']
