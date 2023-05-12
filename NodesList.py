# node 겍체 설계
class Node:
    def __init__(self, data, nextNode=None):
        self.data = data  # 노드에 저장할 대이터
        self.next = nextNode  # 뒤에 연결한 노드를 가리킬 포인트(연결고리)

    def nextNode(self):
        return self.next


# slist 객채 서럐(single linked list)
class SList:
    def __init__(self):
        self.head = None
        self.count = 0  # 리스트에 연결되어 있는 노드의수,

    # 리스트 노트 개수를 보고하는 매소드 정의
    def size(self):
        return self.count

    # 리스트가 비어있는지 여부를 참/거짓으러 보고 비어잇으면 참
    def isEmpty(self):
        if self.count == 0:
            return True  # 비어있음
        else:
            return False

    # 리스트 맨앞에 있는 새노드를 생성하여 연결한다
    def insertFront(self, item):
        # item 을 담을 새 노드를 먼저 생성한다
        newNode = Node(item)

        # 빈 리스트이면
        if self.isEmpty():
            self.head = newNode  # head -> newnode
        else:
            newNode.next = self.head
            self.head = newNode

        # 노드 개수 속성 증가
        self.count += 1

    #리스트의 현재 연결상태를 출력하는 매소드 정의
    def printList(self):
        print("heard->",end="")
        현재노드 = self.head

        #현재노드가 node이 될때가지 차레대로 다음노드를 방문하여 출력
        while 현재노드 != None:
            print(f"[{현재노드.data}]->",end="") #현재노드의 값을 출력
            현재노드 = 현재노드.next

        print("{End}")

    #리스트의 맨뒤에 새노드 추가 연결하는 매소드
    def append(self, item):
        newNode = Node(item)    #우선 새노드 생성
        if self.isEmpty():      #빈리스트 이면
            self.head = newNode #새노드를 첫 노드로 연결
        else:
            현재노드 = self.head #첫노드 부터 탐새시작

            #새노드를 연결할 마지막 노드를 찻는다
            while 현재노드.next != None:   #다음 노드가 정상노드이면
                현재노드 = 현재노드.next    #다음노드로 이동

            #마지막 노드뒤에 새노드를 연결한다
            현재노드.next = newNode

        #마지막에 추가된 노드 개수(+1)를 추가한다
        self.count += 1

    # 리스트에서 주어진 갑(value)을 가진 노드가 있는지 탐색하고 결과를 반환한다.
    #반환값: 찾은 겍체/Node(찾는 겍체가 없을때)
    def isThere(self, value):
        현재노드 = self.head

        # 첫 노드부터 마지막 노드까지 발견될때까지
        while 현재노드 != None:
            if 현재노드.data == value:
                return 현재노드.data
            else:
                현재노드 = 현재노드.next

        # while 반복문이 종료, 찾는 노드(value) 없음
        return None

    #리스트 에서 특정겍체를 지정하여 삭제한다
    #삭제된 삭제한 노드 객체(리스트에서 제외된 노드임)
    def remove(self, targetNode):
        # 삭제할 노드가 첫 노드이면
        if self.head == targetNode:
            self.head = targetNode.next
        else:
            #targetNode을 가리키는지 전노드를 찾는다.
            #삭제후 리스트 연결구조유지하기 위해
            현재노드 = self.head
            while 현재노드.next != targetNode:
                현재노드 = 현재노드.next

            현재노드.next = targetNode.next

        #리스트의 노드 개수를 1 줄인다
        self.count -= 1

        #삭제한 노드의 next속서을 지우고 반환
        targetNode.next = None
        return targetNode


    # 리스트의 target 노드잎에 newNode 삽입한다
    def insertBefore(self, target, newNode):

        # 타겟노드가 리스트의head이면
        if target == self.head:
            self.insertFront(newNode)
        else:
            직전노드 = self.head
            # target의 직전 노드를 먼저 찾는다.
            while 직전노드 != target:
                직전노드 = 직전노드.next
            #직전노드와 target 사이의 newNode를 삽입하는 연결처리를한다
            직전노드.next = newNode
            newNode.next = target
        self.count+=1

















# =============================================================================================================================

