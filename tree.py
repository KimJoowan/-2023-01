from  dblList import * #Queie를 사욜하기 위해
class BTree:
    def __init__(self, value):
        self.item = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"[{self.item}]"

    def preOrder(self):
        print(self, " ", end="")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self, " ", end="")
        if self.right:
            self.right.inOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self, " ", end="")

    def levelOrder(self):
        queue = Queue()
        queue.add(self)

        print("[levelOrder]:", end="")
        while not queue.isEmpty():
            visitNode = queue.remove()
            print(visitNode, " ", end="")
            if visitNode.left:
                queue.add(visitNode.left)
            if visitNode.right:
                queue.add(visitNode.right)
        print(".")

    def height(self):
        if self.left == None and self.right == None:
            return 1
        elif self.left == None:
            return self.right.height()+1
        elif self.right == None:
            return self.left.height()+1
        else:
            return max(self.left.height(), self.left.height())+1



    #[name,1,2,3,4]로 출력
    def toList(self):
        return None
    
    #불안전 여부
    def isComplete(self):
        return None
        
        
        
        
        
        
        
        
        















# ==============================================================================================
treeA = BTree("A")
treeB = BTree("B")
treeC = BTree("C")
treeD = BTree("D")
treeE = BTree("E")
treeF = BTree("F")

# tree 연결하기
treeA.left = treeB
treeA.right = treeC
treeB.left = treeD
treeB.right = treeE
treeC.left = treeF

# tree 방문하기
treeA.levelOrder()
print(treeA.height())

