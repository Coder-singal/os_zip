class Node:
    def __init__(self, id, total_nodes):
        self.id = id
        self.total = total_nodes
        self.timestamp = 0
        self.replies_received = 0
        self.requesting = False

    def request_cs(self, others):
        self.requesting = True
        self.timestamp += 1
        self.replies_received = 0
        print(f"Node {self.id} requesting CS with TS {self.timestamp}")
        
        for node in others:
            node.receive_request(self.id, self.timestamp, self)

    def receive_request(self, sender_id, sender_ts, sender_obj):
        # Simplification: If not requesting, just reply
        if not self.requesting or sender_ts < self.timestamp:
            print(f"Node {self.id} replies to Node {sender_id}")
            sender_obj.receive_reply()
        else:
            print(f"Node {self.id} DEFERS reply to Node {sender_id}")

    def receive_reply(self):
        self.replies_received += 1
        if self.replies_received == self.total - 1:
            print(f"Node {self.id} ENTERING Critical Section")
            self.requesting = False

n1 = Node(1, 2)
n2 = Node(2, 2)

# N1 wants to enter
n1.request_cs([n2])