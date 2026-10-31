class LRUCache:
    
    
    def __init__(self, capacity: int):
        self.mp = OrderedDict()
        self.leng = capacity

    def get(self, key: int) -> int:
        if key in self.mp:
            self.mp.move_to_end(key)
            return self.mp[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.mp[key] = value
            self.mp.move_to_end(key)
        else:
            if len(self.mp) >= self.leng:
                self.mp.popitem(last=False)
            self.mp[key] = value
        
