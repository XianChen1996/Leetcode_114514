from collections import deque


class LRUCache:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.queue = deque()
        self.hash_map = dict()

    def is_queue_full(self):
        return len(self.queue) == self.cache_size

    def put(self, key, value):
        if key not in self.hash_map:
            if self.is_queue_full():
                pop_key = self.queue.pop()
                self.hash_map.pop(pop_key)
                #字典 pop() 方法删除字典给定键 key 及对应的值，
                self.queue.appendleft(key)
                self.hash_map[key] = value
            else:
                self.queue.appendleft(key)
                self.hash_map[key] = value
        else:
             self.queue.remove(key)
             self.queue.appendleft(key)
             self.hash_map[key] = value

###万一有重叠了，直接移除并覆盖



    def get(self, key):
        if key not in self.hash_map:
            return -1
        else:
            self.queue.remove(key)
            self.queue.appendleft(key)
            return self.hash_map[key]


if __name__ == '__main__':
    # 設定 cache 大小為 3
    lru_cache = LRUCache(2)

    lru_cache.put(2, 1)
    lru_cache.put(1, 1)
    lru_cache.put(2, 3)
    lru_cache.put(4, 1)

    print(lru_cache.get(1))
    print(lru_cache.get(2))
