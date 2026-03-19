import socket
from core.logger import logger

def capture_packets(host="127.0.0.1", port=9000, count=5):
    """
    Capture TCP packets sent to a local port.
    Returns list of captured packet data.
    """
    captured = []
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(5)
        logger.log("INFO", f"Listening on {host}:{port}")
        
        while len(captured) < count:
            client, addr = s.accept()
            data = client.recv(2048)
            captured.append(data)
            logger.log("INFO", f"Captured packet from {addr}")
            client.close()
    except Exception as e:
        logger.log("ERROR", f"Packet capture error: {e}")
    finally:
        s.close()
    
    return captured
