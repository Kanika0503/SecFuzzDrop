import streamlit as st
from fuzzy_engine import evaluate_node
from iwd_optimizer import optimize_paths
from falco_simulator import simulate_falco_alerts
from cadvisor_simulator import simulate_cadvisor_metrics
from security_rules import apply_security_rules
import streamlit.components.v1 as components
from security_engine import detect_side_channel_attack, detect_fake_container

# Optional: simulate dummy metrics
def simulate_cadvisor_metrics():
    return {
        "cpu_usage": "35%",
        "memory_usage": "512MB",
        "disk_io": "20MB/s",
        "network_io": "50kB/s",
        "container_count": 5
    }

def main():
    st.set_page_config(page_title="Secure Container Scheduler", layout="wide")
    st.title("🛡 Secure Container Scheduler using Fuzzy + IWD Algorithm")
    st.markdown("---")

    num_containers = st.number_input("🔢 Enter number of containers", min_value=1, max_value=20, value=3)
    st.markdown("### 📦 Container Resource Evaluation (Fuzzy Logic)")

    nodes = []
    for i in range(num_containers):
        score = evaluate_node(
            cpu_val=50 + i*5,
            mem_val=2048 - i*100,
            net_val=50 + i*2,
            latency_val=20 + i*3,
            temp_val=45 + i,
            attack_val=10 + i,
            threat_val=i
        )
        nodes.append({"container_id": f"c{i+1}", "score": score})
    st.table(nodes)

    st.markdown("### 🧠 Optimized Node Assignment (IWD Algorithm)")
    assigned_nodes = apply_iwd(nodes)
    st.table(assigned_nodes)

    st.markdown("### 🔐 Security Check")
    col1, col2 = st.columns(2)

    with col1:
        if detect_side_channel_attack():
            st.error("⚠️ Side Channel Attack Detected!")
        else:
            st.success("✅ No Side Channel Attack")

    with col2:
        if detect_fake_container():
            st.error("⚠️ Fake Container Injection Detected!")
        else:
            st.success("✅ All Containers Verified")

    st.markdown("### 📡 Real-time Monitoring with cAdvisor (Docker)")
    st.info("Ensure `cadvisor` is running on `localhost:8080` via Docker before using this view.")

    components.iframe("http://localhost:8080", width=1000, height=600)

    st.markdown("### 📊 Simulated Metrics Snapshot (Optional JSON View)")
    st.json(simulate_cadvisor_metrics())

if __name__ == "__main__":
    main()

def main():
    st.set_page_config(page_title="Secure Container Scheduler", layout="wide")
    st.title("🔐 Secure Container Scheduler using Fuzzy Logic & IWD Optimization")

    num_containers = st.slider("Select Number of Containers", 1, 10, 3)

    st.subheader("🧠 Fuzzy Node Evaluation Scores")
    node_scores = []

    for i in range(num_containers):
        cpu_val = 40 + i * 5     # Example values for simulation
        mem_val = 50 + i * 4
        latency_val = 60 - i * 3
        threat_val = min(10, i * 2)

        score = evaluate_node(
            cpu_val=cpu_val,
            mem_val=mem_val,
            latency_val=latency_val,
            threat_val=threat_val
        )

        node_scores.append({
            "Container": f"C{i + 1}",
            "CPU": cpu_val,
            "Memory": mem_val,
            "Latency": latency_val,
            "Threat Level": threat_val,
            "Fuzzy Score": round(score, 2)
        })

    st.table(node_scores)

    st.subheader("📍 Optimized Scheduling using IWD Algorithm")
    st.info("IWD algorithm will be applied here for container-node mapping with anti-collocation & anti-affinity rules (implementation in progress or simulated below).")

    # Display dummy optimized assignment
    for i, ns in enumerate(node_scores):
        st.write(f"✅ {ns['Container']} scheduled to Node-{(i % 3) + 1} | Score: {ns['Fuzzy Score']}")

    st.markdown("---")
    st.caption("Real-time monitoring via Falco & cAdvisor not shown in web GUI. Please check Docker-based monitoring setup separately.")
st.subheader("📊 Real-Time Resource Monitoring")

# Embed cAdvisor live
st.markdown("### Embedded cAdvisor Dashboard")
components.iframe("http://localhost:8080", width=1000, height=600)

# Optional instructions
st.info("For real-time security alerts, use `docker logs -f falco` in your terminal.")
if __name__ == "__main__":
    main()
