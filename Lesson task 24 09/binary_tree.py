class Tree:

    def __init__(self):
        self.root = None

    def search(self, value: int):
        found_node = self._search(self.root, value)
        if found_node == None:
            return False
        return True

    def delete(self, value):
        pass

    def max_value(self, value):
        pass

    def min_value(self):
        pass

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)

            return

        return self._insert(self.root, value)


    def _insert(self, current_node, value):
        #go to right
        if value > self.root.value:
            # add to the right
            if current_node.right is None:
                current_node.right = Node(value, current_node)
                return
            #search for a proper position in right branch
            return self._insert(current_node.right, value)
        else:
            # add to the left
            if current_node.left is None:
                current_node.left = Node(value, current_node)
                return
            return self._insert(current_node.left, value)

    def _search(self, node_to_check, value):

        #no more nodes, our parent is a leaf
        #we found: searched value is equal to the node
        if (node_to_check == None) or (node_to_check == value):
            return node_to_check

        #we found: searched value is equal to the node
        if node_to_check.value == value:
            return node_to_check

        if value > node_to_check.value:
            # go right
            return self._search(node_to_check.right, value)
        else:
             # go left
             return self._search(node_to_check.left, value)


    def output_tree(self):
        if (self.root != None):
            self._output_tree(self.root)

    def _output_tree(self, Node):
        if (Node != None):
            self._output_tree(Node.left)
            print( str(Node.value), end= ' ' )
            self._output_tree(Node.right)
            
class Node:
    def __init__(self, value, parent=None):
        self.right = None
        self.left = None
        self.parent = None
        self.value = value

    def __str__(self):
        for items in self.value:
            return items

        #return 'Node [' + str(self.value) + ']'



tree = Tree()
tree = Tree()
tree.insert(43)
tree.insert(12)
tree.insert(4)
tree.insert(8)
tree.insert(31)
tree.insert(56)
tree.insert(-2)
tree.insert(1)
print(tree.output_tree())