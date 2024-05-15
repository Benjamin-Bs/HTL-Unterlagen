import socket

HOST = '127.0.0.1'
PORT = 9999

# AF_INET => TCP
# SOCK_STREAM => IPv4

myserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myserver.bind((HOST, PORT))


def get_data(client_socket):
    header = client_socket.recv(1024)
    if not header: return None

    data_length = int.from_bytes(header, byteorder='big')

    data = client_socket.recv(data_length).decode('utf-8')
    return data


myserver.listen(5)

while True:
    conn, addr = myserver.accept()
    print("Connected by", addr)

    # Daten vom Client empfangen
    received_data = get_data(conn)

    if received_data:
        print("Received data:", received_data)
    else:
        print("Connection closed by client.")

    message = conn.recv(1024).decode("utf-8")
    print("Message: ", message)

    conn.send("message received".encode("utf-8"))

    conn.close()
    print("Connection closed")
