#2164_카드2
#구현, 큐

N = int(input())

class Queue :
    def __init__(self, capacity) :
        self.capacity = capacity + 1
        self.queue = [0 for _ in range(self.capacity)]
        self.front = 0
        self.rear = 0
    
    def is_full(self) :
        return self.front == (self.rear+1) % self.capacity
    
    def is_empty(self) :
        return self.front == self.rear
    
    def enqueue(self, x) :
        if self.is_full() :
            return
        else :
            self.queue[self.rear] = x
            self.rear = (self.rear + 1) % self.capacity
            return
    def dequeue(self) :
        if self.is_empty() :
            return
        else :
            value = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            return value
    
    def size(self) :
        return (self.rear - self.front + self.capacity) % self.capacity
    

queue = Queue(N)

for i in range(1, N+1) :
    queue.enqueue(i)

while queue.size() > 1 :
    queue.dequeue()
    queue.enqueue(queue.dequeue())

print(queue.dequeue())