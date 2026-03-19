from modules import capture, analyze

# Capture packets
packets = capture.run(host="127.0.0.1", port=9000, count=5)

# Analyze captured packets
results = analyze.run(packets)

# Display results
print("\nPHOENIX Packet Analysis Results:")
for r in results:
    print(f"Packet {r['packet_number']}: {r['length']} bytes")
