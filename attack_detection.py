from collections import defaultdict

request_count = defaultdict(int)

def analyze_traffic(packet):
    ip_src = packet[IP].src

    request_count[ip_src] += 1

    if request_count[ip_src] > 100:
        print(f"Potential DDoS attack detected from {ip_src}")

        from mitigation import mitigate_attack
        mitigate_attack(ip_src)

