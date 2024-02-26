from scapy.all import *

def port_scanner(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port+1):
        packet = IP(dst=host)/TCP(dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)
        if response is not None and response.haslayer(TCP):
            if response[TCP].flags == 0x12:  # SYN-ACK
                open_ports.append(port)
                sr(IP(dst=host)/TCP(dport=port, flags="R"), timeout=1, verbose=0)
    return open_ports

host = '127.0.0.1'  # Replace with the target IP or hostname
start_port = 1
end_port = 1024   # Scan up to the first 1024 ports (the well-known ports)

open_ports = port_scanner(host, start_port, end_port)
if open_ports:
    print(f"Open ports on {host} within the range {start_port}-{end_port} are:")
    print(open_ports)
else:
    print(f"No open ports found on {host} within the range {start_port}-{end_port}.")
