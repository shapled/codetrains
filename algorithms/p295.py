# -*- coding: utf-8 -*-


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # (i-1)//2 -> i -> 2*i+1, 2*i+2
        self.min_heap = []
        self.max_heap = []

    def add_to_min_heap(self, v):
        self.min_heap.append(v)
        pos = len(self.min_heap) - 1
        while pos >= 0:
            parent = (pos - 1) // 2
            if parent < 0 or self.min_heap[parent] <= self.min_heap[pos]:
                break
            self.min_heap[parent], self.min_heap[pos] = self.min_heap[pos], self.min_heap[parent]
            pos = parent

    def add_to_max_heap(self, v):
        self.max_heap.append(v)
        pos = len(self.max_heap) - 1
        while pos >= 0:
            parent = (pos - 1) // 2
            if parent < 0 or self.max_heap[parent] >= self.max_heap[pos]:
                break
            self.max_heap[parent], self.max_heap[pos] = self.max_heap[pos], self.max_heap[parent]
            pos = parent

    def update_min_first(self):
        pos = 0
        while pos < len(self.min_heap):
            child1 = 2 * pos + 1
            child2 = 2 * pos + 2
            child = None
            if child1 < len(self.min_heap) and self.min_heap[child1] < self.min_heap[pos]:
                child = child1
            if child2 < len(self.min_heap) and self.min_heap[child2] < self.min_heap[pos] \
                    and self.min_heap[child2] < self.min_heap[child1]:
                child = child2
            if child is None:
                break
            self.min_heap[child], self.min_heap[pos] = self.min_heap[pos], self.min_heap[child]
            pos = child
    
    def update_max_first(self):
        pos = 0
        while pos < len(self.max_heap):
            child1 = 2 * pos + 1
            child2 = 2 * pos + 2
            child = None
            if child1 < len(self.max_heap) and self.max_heap[child1] > self.max_heap[pos]:
                child = child1
            if child2 < len(self.max_heap) and self.max_heap[child2] > self.max_heap[pos] \
                    and self.max_heap[child2] > self.max_heap[child1]:
                child = child2
            if child is None:
                break
            self.max_heap[child], self.max_heap[pos] = self.max_heap[pos], self.max_heap[child]
            pos = child

    def rebalance(self):
        while len(self.min_heap) - len(self.max_heap) > 1:
            self.add_to_max_heap(self.min_heap[0])
            self.min_heap[0] = self.min_heap.pop()
            self.update_min_first()
        while len(self.max_heap) - len(self.min_heap) > 1:
            self.add_to_min_heap(self.max_heap[0])
            self.max_heap[0] = self.max_heap.pop()
            self.update_max_first()

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            self.add_to_min_heap(num)
        elif self.max_heap and num < self.max_heap[0]:
            self.add_to_max_heap(num)
        elif len(self.min_heap) < len(self.max_heap):
            self.add_to_min_heap(num)
        else:
            self.add_to_max_heap(num)
        self.rebalance()

    def findMedian(self) -> float:
        v1 = self.max_heap[0] if self.max_heap else 0
        v2 = self.min_heap[0] if self.min_heap else 0
        if len(self.max_heap) > len(self.min_heap):
            return v1
        elif len(self.max_heap) < len(self.min_heap):
            return v2
        else:
            return (v1 + v2) / 2


if __name__ == '__main__':
    f = MedianFinder()
    assert f.findMedian() == 0
    f.addNum(1)
    assert f.findMedian() == 1
    f.addNum(2)
    assert f.findMedian() == 1.5
    f.addNum(3)
    assert f.findMedian() == 2
    for i in range(4, 10):
        f.addNum(i)
    assert f.findMedian() == 5
    for i in range(1, 10):
        f.addNum(i)
    assert f.findMedian() == 5
