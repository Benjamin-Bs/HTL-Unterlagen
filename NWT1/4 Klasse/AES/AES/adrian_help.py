import socket


class ServerInteraction:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.initial_message = self.client_socket.recv(4096).decode()
        self.n = int(self.initial_message.split()[-2])
        self.B = self.n // (3 * 2048)
        self.queries = 0

    def query(self, request):
        req_string = ",".join(map(str, request)) + "\n"
        self.client_socket.sendall(req_string.encode())
        response = self.client_socket.recv(4096).decode()
        self.queries += 1
        return int(response.split()[0])

    def finish_requests(self, array):
        while (self.queries < 10000 - 1):
            self.query([1, 1, 1, 1])
        req_string = "1,1,1,1\n"
        self.client_socket.sendall(req_string.encode())
        response = self.client_socket.recv(4096).decode()
        self.queries += 1
        print(response)

        req_string = ",".join(map(str, array)) + "\n"
        self.client_socket.sendall(req_string.encode())
        response = self.client_socket.recv(4096).decode()
        self.queries += 1
        print(response)

    def close_connection(self):
        self.client_socket.close()


def main():
    chall = ServerInteraction('lwe2048.challs.open.ecsc2024.it', 38018)

    i = 0
    while not (is_all_even(chall)):
        chall.close_connection()
        chall = ServerInteraction('lwe2048.challs.open.ecsc2024.it', 38018)
        i += 1
        print(i)
    print(i)

    result = [
        get_value(chall, 0),
        get_value(chall, 1),
        get_value(chall, 2),
        get_value(chall, 3)
    ]
    chall.finish_requests(result)


def is_all_even(chall):
    half = chall.n // 2

    erg = chall.query([half, half, half, half])

    erg0 = chall.query([half // 2, half, half, half])
    erg1 = chall.query([half, half // 2, half, half])
    erg2 = chall.query([half, half, half // 2, half])
    erg3 = chall.query([half, half, half, half // 2])
    return (erg < chall.B) and (erg0 < chall.B) and (erg1 < chall.B) and (erg2 < chall.B) and (erg3 < chall.B)


def get_value(chall, index):
    half = chall.n // 2
    bottom = 0
    top = chall.n
    i = 1
    n_count = 0
    j = 1

    while (top > bottom):
        array = [half, half, half, half]
        array[index] = i
        erg = chall.query(array)

        new_top = (erg + (n_count) * chall.n) // i
        new_bottom = new_top - (chall.B // i)
        if not ((bottom <= new_top and new_top <= top) or (bottom <= new_bottom and new_bottom <= top)):
            n_count += 1
            new_top = (erg + (n_count) * chall.n) // i
            new_bottom = new_top - (chall.B // i)

        top = new_top
        bottom = new_bottom
        i *= 2
        n_count *= 2
        j += 1

    print(j)
    print("bottom: " + str(bottom))

    return bottom


if __name__ == "__main__":
    main()
