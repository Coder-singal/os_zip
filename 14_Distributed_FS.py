class NameNode:
    def __init__(self):
        self.file_map = {} # Filename -> list of DataNodes

    def register(self, filename, nodes):
        self.file_map[filename] = nodes
        print(f"NameNode: Mapped '{filename}' to nodes {nodes}")

    def get_locations(self, filename):
        return self.file_map.get(filename, [])

class DataNode:
    def __init__(self, id):
        self.id = id
        self.data = {}

    def store(self, filename, content):
        self.data[filename] = content
        print(f"DataNode {self.id}: Stored '{content}' for {filename}")

# Simulation
namenode = NameNode()
dn1 = DataNode(1)
dn2 = DataNode(2)

# Client writes file
filename = "lab_report.txt"
content = "Distributed Systems are cool"

# Sharding/Replication logic
namenode.register(filename, [1, 2])
dn1.store(filename, content)
dn2.store(filename, content)

# Client reads file
locs = namenode.get_locations(filename)
print(f"Client found file at DataNodes: {locs}")