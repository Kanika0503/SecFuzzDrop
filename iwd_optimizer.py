def optimize_paths(container_scores):
    return sorted(container_scores, key=lambda x: -x["score"])
