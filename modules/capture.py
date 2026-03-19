from core.packet import capture_packets

def run(host="127.0.0.1", port=9000, count=5):
    print(f"Capturing {count} packets on {host}:{port}")
    packets = capture_packets(host, port, count)
    return packets
