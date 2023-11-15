class LRUCache:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.cache = {}

    def put(self, key, value):
        if len(self.cache.items()) < self.capacity:
            if key in self.cache:
                calls_cnt = self.cache[key][1]
                self.cache[key] = [value, calls_cnt + 1]
            else:
                self.cache[key] = [value, 1]
        else:
            min_call_cnt = min(cnt[1] for cnt in self.cache.values())
            for key in self.cache.keys():
                if self.cache[key][1] == min_call_cnt:
                    self.cache.pop(key)
                    break

    def get(self, key):
        self.cache[key][1] += 1
        return self.cache[key][0]

cache = LRUCache(4)
cache.put('a',1)
cache.put('a',2)
cache.put('a',3)
print(cache.cache)
