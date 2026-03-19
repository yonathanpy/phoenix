def run(packets):
    """
    Analyze captured packets: return length and simple stats.
    """
    analysis = []
    for i, pkt in enumerate(packets):
        analysis.append({
            "packet_number": i + 1,
            "length": len(pkt)
        })
    return analysis
