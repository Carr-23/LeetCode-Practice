class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lowest = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lowest.remove(key)
            self.lowest.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) == self.capacity:
            popKey = self.lowest.pop(0)
            del self.cache[popKey]
        elif key in self.cache:
            self.lowest.remove(key)
        
        self.lowest.append(key)
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)