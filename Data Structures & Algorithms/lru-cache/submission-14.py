class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = dict()
        self.LRU, self.MRU = ListNode(0,0), ListNode(0,0)

        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

        #LRU <-> MRU
    
    def _update_MRU(self, node: ListNode) -> None:
        old_mru = self.MRU.prev
        old_mru.next = node
        node.prev = old_mru

        node.next = self.MRU
        self.MRU.prev = node

    def _remove_node(self, node: ListNode) -> None:
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._remove_node(node)
            self._update_MRU(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._remove_node(node)
            #create new node w new val
            updated_node = ListNode(key, value)
            self._update_MRU(updated_node)
            self.key_to_node[key] = updated_node
            return
        
        new_node = ListNode(key, value)
        self._update_MRU(new_node)
        self.key_to_node[key] = new_node
        if len(self.key_to_node) > self.capacity:
            print(key)
            node_to_evict = self.LRU.next
            del self.key_to_node[node_to_evict.key]
            self._remove_node(node_to_evict)
            
        


class ListNode:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
