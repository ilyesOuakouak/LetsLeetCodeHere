class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        
    def remove(self, node):
        a = node.prev
        b = node.next
        
        a.next = b
        b.prev = a 
        
    def add_front(self, node):
        first = self.head.next
        node.prev = self.head
        node.next = first
        first.prev = node
        self.head.next = node
        
    def get(self, key):
        if key not in self.map:
            return -1
        
        node = self.map[key]
        self.remove(node)
        self.add_front(node)
        
        return node.value
    
    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.value = value
            
            self.remove(node)
            self.add_front(node)
        else:
            node = Node(key, value)
            if len(self.map) >= self.capacity:
                oldest = self.tail.prev
                self.remove(oldest)
                del self.map[oldest.key]
            self.add_front(node)
            self.map[key] = node 
            