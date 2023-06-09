from dblList import * # queue를 사용하기 위해
class BTree:
    def __init__(self, value):
        self.item = value
        self.left = None
        self.right = None

    def __str__(self):
        #return f"[{self.item}]"
        return self.node()

    #자식이 있으면 ture
    def hasNoChild(self):
        return self.left == None and self.right == None


    def node(self): #노드의 현재 상황(왼쪽값 자신 오른족값)을 문자열 로반환한다
        r = "[ "
        if self.left:
            r += str(self.left.item) + " <- "
        else:
            r += "None <- "
        r += str(self.item)
        if self.right:
            r += " " \
                 "-> "+ str(self.right.item) + "]"
        else:
            r += "-> None ]"
        return  r

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

    def checkHeight(self):
        if self.left == None and self.right == None:
            return 1
        elif self.left == None:
            return self.right.checkHeight()+1
        elif self.right == None:
            return self.left.checkHeight()+1
        else:
            return max(self.left.checkHeight (), self.left.checkHeight())+1

    # [name,1,2,3,4]로 출력
    def toList(self):

        if not self.isComplete():
            print("완전이진 트리가 아님니다.")
            return None
        lst = [None] # 반환할 리스트 초기화
        queue = Queue()
        queue.add(self)

        while not queue.isEmpty():
            visitNode = queue.remove()
            lst.append(visitNode.item)
            if visitNode.left:
                queue.add(visitNode.left)
            if visitNode.right:
                queue.add(visitNode.right)
        return lst

    # 불안전 여부
    def isComplete(self):
        queue = Queue()
        queue.add(self)
        flag = False # leaf 노드가 발견되면 Ture 설정 예정.

        while not queue.isEmpty():
            visitNode = queue.remove()

            if visitNode.left:# 현재노드의 왼쪽자식이 잇고
                if flag:       # 이전에 이파이 노드가 발견된 상황이면
                    return False# 완전이진트리가 안됌
                else:
                    queue.add(visitNode.left)#다음 조사를 위해 왼쪽자식 을 큐에 저장.
            else:
                flag = True#왼쪽자식의 왼쪽 자식이 없으면 이진트리가 아닐 조건 설정.

            if visitNode.right: #현재노드의 오른쪽쪽자식이 있다면
                if flag:#현재노드의 왼쪽자식이 없엇다면 (flag 가 True인상황)
                    return False
                else:
                    queue.add(visitNode.right)
            else:
                flag = True

        return True #모든 노드들의 대한 조치가 끝타면 여기까지 오면 완전이진트리가 맞음


#-===================================================================================
# 이진 탐색트리 (Binary Search Tree BST)
#=====================================================================================
class BSTree(BTree):
    # tree에서 중복돼는 값은 존재하지않는것 으로 구현
    # 중복값 을 허용하는 트리 구성은 코드 수정 필요.
    def insert(self, value):
        if value < self.item:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTree(value)
        elif value > self.item:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTree(value)
        else:
            pass

    #BSTree 에서 value 값을 자긴 노드를 찻아 노드를 반환한다.
    def find(self, value):
        if value == self.item:#찾는 노드가 자신이면 자신(self)을 반환
            return self
        if value < self.item: # 찾는 값이 본인보다 작으면 왼쪽자식에개 위혐하고 결과를 토스
            if self.left:
                return self.left.find(value)
            else:      #없으면 찻는 값이 없으므로 None
                return None
        else:
            if self.right:
                return self.right.find(value)
            else:
                return None

    #BSTree 에서 가장 작은 값 찻아서 반환하기
    def minunumvalueR(self):
        if self.left:
            return self.left.minunumvalue()
        else:
            return self.item

    def minunumvalue(self):
        correntNode = self
        while correntNode.left:
            correntNode = correntNode.left

        return correntNode.item

    def minunumnode(self):
        correntNode = self
        while correntNode.left:
            correntNode = correntNode.left
        return correntNode

    #주어진 트리에서 가장 작은 값을 찻아서 삭제한다.
    def deleteMinimum(self):
        if self.left == None:
            return self.right
        self.left = self.left.deleteMinimum()
        return self

    #BSTree 에서 값을 가진 노드를 찻아서 삭제하고 BSTree를 유지할수있게 수정한다
    def deletevalue(self, value):
        if value < self.item: # 찻는값이 현재노드보다 작은경우
            if self.left: # 왼쪽자식이 있으면 왼쪽 자식에게 떠넘기고 겱과를(왼쪽의 root)로 업데이트
                self.left = self.left.deletevalue(value)
            else:
                return self
        elif value > self.item:
            if self.right:
                self.right = self.right.deletevalue(value)
            else:
                return self
        else: #현재노드가 삭제 대상인 경우
            if self.hasNoChild():
                return None
            if self.left == None:
                return self.right
            if self.right == None:
                return self.left

            taget = self
            seccessor = taget.right.minunumnode()
            seccessor.right = taget.right.deleteMinimum()
            seccessor.left = taget.left
            return seccessor
        return self #현재 노드가 살아있는 경우 현재노드가 계속 보스임을 부모에게 날닌다.

#=============================================================================================================

root = BSTree(100)
root.insert(200)
root.insert(150)
root.insert(70)
root.insert(80)
root.insert(300)
root.insert(350)
root.insert(1050)

print("Bofors: ", root)
root = root.deletevalue(100)
print("After: ", root)
print(root.find(200))









