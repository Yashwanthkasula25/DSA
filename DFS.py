class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)#

    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# -------------------------------
# Example Usage
# -------------------------------
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "F")
g.add_edge("E", "F")

print("Graph:")
g.print_graph()

print("\nStarting DFS from node 'A':")
g.dfs("A")
