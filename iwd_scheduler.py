import random

def iwd_schedule(nodes, containers):
    container_allocation = {}
    visited_nodes = set()
    for container in containers:
        best_node = None
        best_score = -1
        for node in nodes:
            if node['id'] in visited_nodes:
                continue
            score = node['score']
            if score > best_score:
                best_score = score
                best_node = node
        if best_node:
            container_allocation[container] = best_node['id']
            visited_nodes.add(best_node['id'])
    return container_allocation