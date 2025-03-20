#Creating node structure
class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
#Inserting Elements/Value in Tree
    def insert(self, value):
        if self.root is None:
            self.root = Treenode(value)
            print(f"{value} inserted!")
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Treenode(value)
                print(f"{value} inserted!")
            else:
                self._insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Treenode(value)
                print(f"{value} inserted!")
            else:
                self._insert(current_node.right, value)

#prefix Printing
    def prefix(self, node):
        if node is None:
            return ""
        return str(node.value) +" " + self.prefix(node.left) + self.prefix(node.right)
#Postfix Printing
    def postfix(self, node):
            if node is None:
                return ""
            return  self.postfix(node.left) + self.postfix(node.right) + " " + str(node.value)
#Postfix Printing
    def Infix(self, node):
            if node is None:
                return ""
            return  self.Infix(node.left) + " " + str(node.value) + self.Infix(node.right)
#Inserting Value in insert() method
tree = BinaryTree()
elements = []
n = int(input("Enter size/Elements of/in Tree:"))
for i in range(n):
    element = int(input(f"Entering {i+1}th Element: "))
    elements.append(element)

for element in elements:
    tree.insert(element)
#Printing the prefix anf postfix
print("\nPrefix Expression (Preorder Traversal):")
print(tree.prefix(tree.root))

print("Converting in postfix")
print(tree.postfix(tree.root))

print("Converting in Infix")
print(tree.Infix(tree.root))
