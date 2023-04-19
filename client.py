import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 1234))

    source = input('Enter the source vertex: ')
    server_socket.sendall(source.encode())

    data = server_socket.recv(1024).decode()
    distances = eval(data)

    print(f'Distances from source vertex {source}: {distances}')

    server_socket.close()

if __name__ == '__main__':
    main()
