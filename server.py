import socket
from os import path, listdir
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
count = 0
# Hashmap of Data
data_to_return = {}

sock = socket.socket(
    socket.AF_INET,  # IPV4
    socket.SOCK_DGRAM  # UDP
)

sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)

    f = []

    onlyfiles = [f for f in listdir(data) if path.isfile(path.join(data, f))]

    print(onlyfiles)

    for file in onlyfiles:

        count += 1

        # Array of Data
        file_spec = (
            str(path.basename(path.join(data, file))),
            str(path.getsize(path.join(data, file))),
            str(path.getmtime(path.join(data, file)))
        )

        data_to_return.update({count: file_spec})

    # print(base_name)
    print(
        data_to_return.get()
    )
