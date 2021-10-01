from heapq import  heappop
class Element:

    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue():
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def search(self, value):
        for i in range(len(self.heap)):
            if self.heap[i].value == value:
                return "element exists",True
        return "there is no such value"

    def peek(self):
        self.heap.pop()
        return "peek value ",self.heap[0].value


    def pop(self):
        self.heap[len(self.heap) - 1], self.heap[0] = self.heap[0], self.heap[len(self.heap) - 1]
        deleted = self.heap.pop()
        self.goUp(0)
        return "popped value", deleted.value


    def add(self, value, priority):
        self.heap.append(Element(value, priority))
        # adding element to  the end
        self.goUp(len(self) - 1)



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


if __name__ == '__main__':
    priority = PriorityQueue()
    priority.add(2, 4)
    priority.add(5, 1)
    priority.add(1, 7)
    priority.add(4, 8)
    print(priority.peek())
    print(priority.search(4))
    print(priority.pop())





