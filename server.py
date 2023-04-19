import socket
import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = [[] for i in range(vertices)]

    def add_edge(self, source, dest, weight):
        self.edges[source].append((dest, weight))
        self.edges[dest].append((source, weight))

    def dijkstra(self, source):
        heap = [(0, source)]
        visited = [False] * self.vertices
        distances = [float('inf')] * self.vertices
        distances[source] = 0

        while heap:
            (distance, current) = heapq.heappop(heap)
            visited[current] = True

            for (neighbor, weight) in self.edges[current]:
                if not visited[neighbor]:
                    new_distance = distances[current] + weight

                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heapq.heappush(heap, (new_distance, neighbor))

        return distances

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname=socket.gethostname()
    ip=socket.gethostbyname(hostname)
    print(f"Connected to {ip}")
    server_socket.bind((ip, 1234))
    server_socket.listen()

    print('Server started. Listening on port 1234.')

    while True:
        (client_socket, address) = server_socket.accept()
        print(f'Client connected from {address}')

        data = client_socket.recv(1024).decode()
        source = int(data)

        graph = Graph(9)
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 8, 2)
        graph.add_edge(1, 2, 7)
        graph.add_edge(1, 6, 3)
        graph.add_edge(2, 3, 8)
        graph.add_edge(2, 5, 5)
        graph.add_edge(3, 4, 4)
        graph.add_edge(5, 7, 2)
        graph.add_edge(2, 7, 7)
        graph.add_edge(6, 2, 2)
        graph.add_edge(6, 5, 6)
        graph.add_edge(7, 3, 3)
        graph.add_edge(8, 1, 2)
        graph.add_edge(8, 5, 9)

        distances = graph.dijkstra(source)

        client_socket.sendall(str(distances).encode())

        client_socket.close()

if __name__ == '__main__':
    main()
