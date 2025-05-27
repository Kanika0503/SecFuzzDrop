import sys
import os
sys.path.append("D:/Test/secure_container_scheduler")
import streamlit as st
from fuzzy_logic.fuzzy_engine import evaluate_node
from iwd_algorithm.iwd_scheduler import iwd_schedule
from monitoring.falco_listener import simulate_falco_alerts

def main():
    st.title("SecuFuzzDrop:Secure Fuzzy based and Intelligent Water Drop Alogirhtm based Container Scheduling")

    container_count = st.number_input("Enter number of containers", min_value=1, max_value=100, value=5)
    if st.button("Schedule"):
        nodes = []
        for i in range(5):
            node = {
                "id": f"Node-{i+1}",
                "score": evaluate_node(
                    cpu_val=50 + i*5,
                    memory_val=60 + i*5,
                    trust_val=7 - i,
                    latency_val=20 + i*3,
                    load_val=50 - i*5,
                    threat_val=i
                )
            }
            nodes.append(node)

        containers = [f"Container-{i+1}" for i in range(container_count)]
        allocation = iwd_schedule(nodes, containers)

        st.subheader("Container Allocation:")
        for container, node in allocation.items():
            st.write(f"{container} → {node}")

        st.subheader("Falco Security Alerts:")
        alerts = simulate_falco_alerts()
        for alert in alerts:
            st.warning(f"{alert['type']} detected on {alert['node']}")

if __name__ == "__main__":
    main()
