import heapq

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0
      

def dijkstra(graph, start):
    heap = BinaryHeap()
    heap.push((0, start))
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    shortest_path_tree = {}

    while not heap.is_empty():
        current_distance, current_vertex = heap.pop()

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path_tree[neighbor] = current_vertex
                heap.push((distance, neighbor))

    return distances, shortest_path_tree

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

distances, shortest_path_tree = dijkstra(graph, 'A')
print("Відстані: ", distances)
print("Дерево найкоротшого шляху: ", shortest_path_tree)
