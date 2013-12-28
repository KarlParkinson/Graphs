import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def enQueue(self, item):
        heapq.heappush(self.items, item)
        
    def deQueue(self):
        return heapq.heappop(self.items)
    
    def updatePriority(self, item, newPriority):
        self.items[self.items.index(item)] = newPriority
        heapq.heapify(self.items)
        
    def isEmpty(self):
        return len(self.items) == 0
    