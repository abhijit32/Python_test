

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'<Node {self.value}>'

class BinaryTree:
    def __init__(self, head: Node):
        self.head = head

    def add_node(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError ('A node with the value already exists')

            if new_node.value < current_node.value:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break

            elif new_node.value > current_node.value:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = new_node 
                    break

    def inOrder(self):
        self.inOrderRecursive(self.head)

    def inOrderRecursive(self, current_node):
        if not current_node:
            return
        self.inOrderRecursive(current_node.left)
        print(current_node)
        self.inOrderRecursive(current_node.right)

    def findParent(self, value: int):
        pass
    
    def findRightMost(self, node: Node):
        pass



#Add the header of the tree
binaryTree = BinaryTree(Node(9))

#Add the remaining nodes 
binaryTree.add_node(Node(11))
binaryTree.add_node(Node(5))

binaryTree.inOrder()




