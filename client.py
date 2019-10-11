import socket

UDP_IP = "127.0.0.1"  # Localhost IP -> This ip will be transmiting the message
UDP_PORT = 5005  # This Port will be transmiting the message
UDP_Message = "Hey, I'm the Server"
UDP_FILE_PATH = "C:\\Users\\diogo\\OneDrive - ESTGV\\Engenharia Informatica\\Discos\\"
UDP_NAME_FILE = "ubuntu.iso"

sock = socket.socket(
    socket.AF_INET,  # IPV4
    socket.SOCK_DGRAM  # UDP
)

sock.sendto((UDP_FILE_PATH).encode(), (UDP_IP, UDP_PORT))
