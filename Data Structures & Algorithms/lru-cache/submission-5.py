class Node:

    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyToNode = {}
        self.LEFT, self.RIGHT = Node(0,0), Node(0,0)

        self.LEFT.next = self.RIGHT
        self.RIGHT.prev = self.LEFT
    
    def insert(self, Node):
        temp = self.RIGHT.prev 
        Node.next = self.RIGHT
        self.RIGHT.prev = Node

        temp.next = Node
        Node.prev = temp
    
    def remove(self, Node):
        right_of_node, left_of_node = Node.next, Node.prev
        right_of_node.prev = left_of_node
        left_of_node.next = right_of_node

        

    def get(self, key: int) -> int:
        print(self.keyToNode)
        if key in self.keyToNode:
            self.remove(self.keyToNode[key])
            self.insert(self.keyToNode[key])
            return self.keyToNode[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            self.remove(self.keyToNode[key])
            self.keyToNode[key] = Node(key, value)
            self.insert(self.keyToNode[key])
        else:
            self.keyToNode[key] = Node(key, value)
            self.insert(self.keyToNode[key])
        
        if len(self.keyToNode) > self.capacity:
            key_to_remove = self.LEFT.next.key
            self.remove((self.LEFT.next))
            del self.keyToNode[key_to_remove]




        
