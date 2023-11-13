class LRUCache:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.cache = {}

    def put(self, key, value):
        if len(self.cache.items()) < self.capacity:
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
