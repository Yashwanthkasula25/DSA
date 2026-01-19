class Graph:
    def __init__(self, edges):
        self.graph = {}
        for start, end in edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]
##
    def print_graph(self):
        print("Graph:")
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.find_all_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def find_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph:
            return None
        shortest = None
        for node in self.graph[start]:
            if node not in path:
                sp = self.find_shortest_path(node, end, path)
                if sp:
                    if shortest is None or len(sp) < len(shortest):
                        shortest = sp
        return shortest


# ------------------------------
# Example Usage
# ------------------------------
edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("D", "F"),
    ("E", "F")
]

g = Graph(edges)

g.print_graph()

start = "A"
end = "F"

print(f"\nAll paths from {start} to {end}:")
paths = g.find_all_paths(start, end)
for path in paths:
    print(" -> ".join(path))

print(f"\nShortest path from {start} to {end}:")
shortest = g.find_shortest_path(start, end)
print(" -> ".join(shortest))
