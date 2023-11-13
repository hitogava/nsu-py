from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.cache = OrderedDict()

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def get(self, key):
        self.cache.move_to_end(key)
        return self.cache[key]
