class Node:
    def __init__(self, name):
        self.name, self.data = name, {}

class DFS:
    def __init__(self, nodes):
        self.nodes, self.i = nodes, 0

    def store(self, fname, content):
        n = self.nodes[self.i]
        n.data[fname] = content
        self.i = (self.i + 1) % len(self.nodes)
        print(f"Stored '{fname}' in {n.name}")

    def read(self, fname):
        for n in self.nodes:
            if fname in n.data:
                print(f"{fname} → {n.name}: {n.data[fname]}")
                return
        print("File not found")

    def show(self):
        for n in self.nodes:
            print(n.name, n.data)

nodes = [Node("Node1"), Node("Node2")]
dfs = DFS(nodes)

dfs.store("A.txt", "Hello")
dfs.store("B.txt", "Distributed")
dfs.store("C.txt", "FS")

dfs.read("B.txt")
dfs.show()
