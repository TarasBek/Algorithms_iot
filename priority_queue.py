class Element:

    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def add(self, value, priority):
        self.heap.append(Element(value, priority))
        # adding element to  the end
        self.goUp(len(self) - 1)

    def delete(self):
        self.heap[len(self) - 1], self.heap[0] = self.heap[0], self.heap[len(self) - 1]
        root = self.heap.delete()
        self.goDown(0)
        return root.value

    def goUp(self, index):
        root_index = (index - 1) // 2
        if root_index < 0:
            return
        if self.heap[index].priority > self.heap[root_index].priority:
            self.heap[index], self.heap[root_index] = self.heap[root_index], self.heap[index]
            self.goUp(root_index)

    def goDown(self, index):
        parent = index
        left_child = (index * 2) + 1
        right_child = (index * 2) + 2

        if self.heap[parent] < self.heap[left_child]:
            parent = left_child
        if self.heap[parent] < self.heap[right_child]:
            parent = right_child

        if (self.heap[index] != self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.goDown(index)

    def peek(self):
        return self.heap[0].value

if __name__ == '__main__':
    priority = PriorityQueue()
    priority.add(45, 0)
    priority.add(31, 1)
    priority.add(20, 2)
    priority.add(14, 3)
    priority.add(7, 4)
    priority.add(12, 5)
    priority.add(18, 6)
    priority.add(11, 7)
    priority.add(7, 8)



