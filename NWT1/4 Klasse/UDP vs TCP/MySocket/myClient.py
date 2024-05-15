import socket

HOST = '127.0.0.1'
PORT = 9999

my_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_client.connect((HOST, PORT))


def send_data(server_socket, data):
    data_length = len(data)
    header = data_length.to_bytes(4, byteorder='big')
    server_socket.sendall(header)


# my_client.send("Hello Server".encode('utf-8'))
send_data(my_client, "Hello Server")

print(my_client.recv(1024).decode('utf-8'))

my_client.close()
