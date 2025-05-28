# security/security_engine.py

import random

def detect_side_channel_attack(cpu_usage, net_io, container_id):
    """
    Simulate detection of side-channel attack based on suspicious CPU/network patterns.
    """
    suspicious_cpu_threshold = 85  # %
    suspicious_net_io_threshold = 10000000  # bytes

    if cpu_usage > suspicious_cpu_threshold and net_io > suspicious_net_io_threshold:
        return {
            "container_id": container_id,
            "status": "Alert",
            "type": "Side-Channel Attack Detected"
        }
    else:
        return {
            "container_id": container_id,
            "status": "Safe",
            "type": "No Threat"
        }

def detect_fake_container(container_id, signature_check=True):
    """
    Simulate detection of fake container injection.
    """
    if not signature_check or random.random() > 0.95:
        return {
            "container_id": container_id,
            "status": "Alert",
            "type": "Fake Container Detected"
        }
    else:
        return {
            "container_id": container_id,
            "status": "Safe",
            "type": "Genuine Container"
        }
