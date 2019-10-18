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


buffer = RingBuffer(5)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('g')
buffer.append('h')
buffer.append('i')
print(buffer.get())   # should return ['a', 'b', 'c']
