class MyHashMap:

    def __init__(self):
        self.hashmap = []
    
    def findKey(self, key):
        for i in range(len(self.hashmap)):
            k,v = self.hashmap[i]
            if k == key:
                return i
        return -1
        

    def put(self, key: int, value: int) -> None:
        index = self.findKey(key)
        if index == -1:
            self.hashmap.append([key,value])
        else:
            self.hashmap[index][1] = value

        

    def get(self, key: int) -> int:
        index = self.findKey(key)
        if index == -1:
            return -1
        else:
            return self.hashmap[index][1]
        

    def remove(self, key: int) -> None:
        index = self.findKey(key)
        if index == -1:
            return
        self.hashmap.pop(index)

            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)