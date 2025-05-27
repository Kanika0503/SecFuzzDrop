import streamlit as st
from fuzzy_logic.fuzzy_engine import evaluate_node
from optimizer.iwd_optimizer import optimize_paths
from monitor.falco_simulator import simulate_falco_alerts
from monitor.cadvisor_simulator import simulate_cadvisor_metrics
from utils.security_rules import apply_security_rules

def main():
    st.title("Secure Container Scheduler")

    container_count = st.slider("Select number of containers", 1, 10, 3)
    st.write(f"Scheduling {container_count} containers...")

    container_scores = []
    for i in range(container_count):
        score = evaluate_node(
            cpu_val=50 + i*5,
            mem_val=60 + i*4,
            net_val=70 - i*2,
            latency_val=30 + i,
            disk_val=40 + i*3,
            temp_val=25 + i,
            threat_val=i
        )
        container_scores.append({"container_id": f"c{i}", "score": score})

    st.subheader("Fuzzy Evaluation Scores")
    st.json(container_scores)

    optimized = optimize_paths(container_scores)
    secure = apply_security_rules(optimized)

    st.subheader("Optimized & Secured Scheduling")
    st.json(secure)

    st.subheader("Falco Security Monitoring")
    st.code(simulate_falco_alerts(), language='bash')

    st.subheader("cAdvisor Resource Monitoring")
    st.json(simulate_cadvisor_metrics())

if __name__ == "__main__":
    main()
