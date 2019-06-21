# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, key, value, order):
        self.key = key
        self.value = value
        self.order = order

    def update(self, order, value=None):
        self.order = order
        self.value = self.value if value is None else value

    def __repr__(self):
        return "<order: %s, value: %s>" % (self.order, self.key)


class LRUCache:
    def __init__(self, capacity: int):
        self.cnt = 0
        self.heap = []  # 最小堆, (i-1)//2 -> i -> 2*i+1, 2*i+2
        self.key_to_pos = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.key_to_pos:
            self.cnt += 1
            pos = self.key_to_pos[key]
            node = self.heap[pos]
            node.update(self.cnt)
            self.update(pos)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        self.cnt += 1
        if key in self.key_to_pos:
            pos = self.key_to_pos[key]
            node = self.heap[pos]
            node.update(self.cnt, value)
            self.update(pos)
        else:
            node = Node(key, value, self.cnt)
            if len(self.heap) < self.capacity:
                self.insert(node)
            else:
                self.pop(node)

    def insert(self, node):
        self.heap.append(node)
        pos = len(self.heap) - 1
        self.key_to_pos[node.key] = pos
        if pos == 0:
            return
        parent = (pos - 1) // 2
        while self.heap[parent].order > self.heap[pos].order:
            tmp_node = self.heap[parent]
            self.heap[parent] = self.heap[pos]
            self.heap[pos] = tmp_node
            self.key_to_pos[self.heap[pos].key] = pos
            self.key_to_pos[self.heap[parent].key] = parent
            pos = parent
            if pos == 0:
                break
            parent = (pos - 1) // 2

    def pop(self, node):
        if not self.heap:
            if self.capacity:
                self.heap = [node]
                self.key_to_pos[node.key] = 0
        else:
            del self.key_to_pos[self.heap[0].key]
            self.heap[0] = node
            self.key_to_pos[node.key] = 0
            self.update(0)

    def update(self, pos):
        while True:
            child1 = 2 * pos + 1
            child2 = 2 * pos + 2
            child = None
            if child1 < len(self.heap) \
                    and self.heap[child1].order < self.heap[pos].order:
                child = child1
            if child2 < len(self.heap) \
                    and self.heap[child2].order < self.heap[pos].order \
                    and self.heap[child2].order < self.heap[child1].order:
                child = child2
            if child is None:
                break
            tmp_node = self.heap[child]
            self.heap[child] = self.heap[pos]
            self.heap[pos] = tmp_node
            self.key_to_pos[self.heap[pos].key] = pos
            self.key_to_pos[self.heap[child].key] = child
            pos = child


if __name__ == '__main__':
    # error
    c = LRUCache(2)
    c.put(2, 1)
    c.put(2, 2)
    assert c.get(2) == 2  # 有 update
    c.put(1, 1)
    c.put(4, 1)
    assert c.get(2) == -1

    # mine
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    
    c = LRUCache(0)
    assert c.get(1) == -1
    assert c.get(0) == -1
    c.put(1, 1)
    assert c.get(1) == -1
    
    c = LRUCache(5)
    for i in range(8):  # 7, 6, 5, 4, 3
        c.put(i, i*10)
    assert c.get(5) == 50
    assert c.get(0) == -1
    assert c.get(3) == 30
    assert c.get(4) == 40
    c.put(9, 70)
    assert c.get(6) == -1
    assert c.get(9) == c.get(7) == 70

