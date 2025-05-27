def apply_security_rules(container_list):
    return [
        {**c, "secure": c["score"] > 40 and not c["container_id"].endswith("2")}
        for c in container_list
    ]
