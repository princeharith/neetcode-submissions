class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.left, self.right = Node(0,0), Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, curr_node):
        last_MRU = self.right.prev

        last_MRU.next = curr_node
        curr_node.prev = last_MRU

        self.right.prev = curr_node
        curr_node.next = self.right

        self.cache[curr_node.key] = curr_node

    def remove(self, curr_node):
        curr_node.prev.next = curr_node.next
        curr_node.next.prev = curr_node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        
        
        

        
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
