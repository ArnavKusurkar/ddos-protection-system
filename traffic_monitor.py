from scapy.all import sniff, IP
from attack_detection import analyze_traffic

def packet_callback(packet):
    if IP in packet:
        analyze_traffic(packet)

sniff(filter="ip", prn=packet_callback, store=0)
