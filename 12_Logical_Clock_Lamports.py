class LamportProcess:
    def __init__(self, pid):
        self.pid = pid          # process ID (like P1, P2)
        self.clock = 0          # logical clock initialized to 0

    def event(self, name):
        self.clock += 1         # internal event → increase clock
        print(f"Process {self.pid} Event {name}: Clock {self.clock}")

    def send_message(self, receiver):
        self.clock += 1         # before sending → increase clock
        print(f"Process {self.pid} SEND to P{receiver.pid}: Clock {self.clock}")
        receiver.receive_message(self.clock)   # send timestamp to receiver

    def receive_message(self, sender_timestamp):
        # update clock: must be greater than both local & received timestamp
        self.clock = max(self.clock, sender_timestamp) + 1
        print(f"Process {self.pid} RECEIVED: Clock updated to {self.clock}")

# create two processes
p1 = LamportProcess(1)
p2 = LamportProcess(2)

p1.event("A")       # internal event on p1 → clock increments
p2.event("B")       # internal event on p2 → clock increments
p1.send_message(p2) # p1 sends message to p2 → both update clocks
p2.event("C")       # another internal event on p2
