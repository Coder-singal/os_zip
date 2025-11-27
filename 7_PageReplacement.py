def fifo_page_replacement(pages, capacity):
    memory = []
    page_faults = 0
    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) >= capacity:
                memory.pop(0) # Remove first in
            memory.append(page)
    return page_faults

def lru_page_replacement(pages, capacity):
    memory = [] # Using list as a stack for LRU logic
    page_faults = 0
    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) >= capacity:
                memory.pop(0) # Pop least recently used (front of list)
            memory.append(page)
        else:
            # Move accessed page to end (most recently used)
            memory.remove(page)
            memory.append(page)
    return page_faults

pages = [1, 3, 0, 3, 5, 6, 3]
capacity = 3
print(f"FIFO Faults: {fifo_page_replacement(pages, capacity)}")
print(f"LRU Faults:  {lru_page_replacement(pages, capacity)}")
