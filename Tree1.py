class TNode:
    def __init__(self, value):
        self.item = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"[{self.item}]"

class BinaryTree:
    def __init__(self):
        self.root = None

    def perOrder(self, visitNode):
        if visitNode:
            print(visitNode," ", end="")
            if visitNode.left:
                self.perOrder(visitNode.left)
            if visitNode.right:
                self.perOrder(visitNode.right)

    def inOrder(self,visitNode):
        if visitNode:
            if visitNode.left:
                self.inOrder(visitNode.left)
            print(visitNode, " ", end="")
            if visitNode.right:
                self.inOrder(visitNode.right)

    def postOrder(self, visitNode):
        if visitNode:
            if visitNode.left:
                self.postOrder(visitNode.left)
            if visitNode.right:
                self.postOrder(visitNode.right)
            print(visitNode, " ", end="")

#===================================================================================================================================================================================
tree = BinaryTree()


NodeA = TNode("+")
NodeB = TNode("A")
NodeC = TNode("B")
NodeD = TNode("-")

NodeA.left = NodeB
NodeA.right = NodeC
NodeB.left = NodeD



tree.root = NodeA
tree.postOrder(tree.root)

















