class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


a1 = BinaryTreeNode(100)
a2 = BinaryTreeNode(80)
a3 = BinaryTreeNode(120)
a4 = BinaryTreeNode(70)
a5 = BinaryTreeNode(85)
a6 = BinaryTreeNode(110)
a7 = BinaryTreeNode(125)

a1.leftChild = a2
a1.rightChild = a3
a2.leftChild = a4
a2.rightChild = a5
a3.leftChild = a6
a3.rightChild = a7


print("Root Node is:")
print(a1.data)
print("left child of node is:")
print(a1.leftChild.data)
print("right child of node is:")
print(a1.rightChild.data)
print("Node is:")
print(a2.data)
print("left child of node is:")
print(a2.leftChild.data)
print("right child of node is:")
print(a2.rightChild.data)
print("Node is:")
print(a3.data)
print("left child of node is:")
print(a3.leftChild.data)
print("right child of node is:")
print(a3.rightChild.data)
print("Node is:")
print(a4.data)
print("left child of node is:")
print(a4.leftChild)
print("right child of node is:")
print(a4.rightChild)
print("Node is:")
print(a5.data)
print("left child of node is:")
print(a5.leftChild)
print("right child of node is:")
print(a5.rightChild)
print("Node is:")
print(a6.data)
print("left child of node is:")
print(a6.leftChild)
print("right child of node is:")
print(a6.rightChild)
print("Node is:")
print(a7.data)
print("left child of node is:")
print(a7.leftChild)
print("right child of node is:")
print(a7.rightChild)