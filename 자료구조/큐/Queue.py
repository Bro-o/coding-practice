class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        if self.front is None:
            self.front = self.rear = Node(data)
        else:
            node = Node(data)
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return None
        node = self.front
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return node.data

    def is_empty(self):
        return self.front is None
    

def reverse_queue(q: Queue) -> None:
    s = []
    while not q.is_empty():
        s.append(q.dequeue())
    while s:
        q.enqueue(s.pop())

def reverse_queue_recursive(q: Queue) -> None:
    data = q.dequeue()
    reverse_queue_recursive(q)
    q.enqueue(data)

def display(q: Queue) -> None:
    node = q.front
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    q = Queue()

    for i in range(5):
        q.enqueue(i)
    display(q)

    reverse_queue(q)
    display(q)