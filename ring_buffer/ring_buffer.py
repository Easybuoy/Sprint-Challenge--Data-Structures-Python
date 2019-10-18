class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.current < self.capacity:
            self.storage[self.current] = item
            self.current += 1
        else:
            if self.capacity == self.current:
                self.storage[0] = item
                self.current += 1
            else:
                self.storage[self.current - self.capacity] = item
                self.current += 1

    def get(self):
        return list(filter(None, self.storage))
