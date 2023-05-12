class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# ========================================================================================================================
class DList:
    def __init__(self):
        self.head = None    # 리스트의 시작 노드
        self.tail = None    # 리스트의 마지막 노드
        self.count = 0

    def __str__(self):
        retstr = "" # 반환할 문자열(초기값은 빈문자열)
        currentNode = self.head #이중연결리스트 해드부터 차래대러 방문예정
        while currentNode != None:
            # 방문의 data값 retstr에 출력
            retstr += currentNode.data + " "
            currentNode = currentNode.next
        # 누적된 결과 문자열반환
        return retstr




    # 리스트의 첫노드부터 끝까지 차레러 출력

    def show(self, showOrder="FORWARD"):
        if showOrder == "FORWARD":
            현재노드 = self.head
            while (현재노드 != None):
                print(f"[{현재노드.data}]<=>", end="")
                현재노드 = 현재노드.next
            print(f"(Tail : {self.count} 노드)")
            # FORWARD 아닌값이면 역방향으로 출력
        else:
            현재노드 = self.tail
            while(현재노드 != None):
                print(f"[{현재노드.data}]<=>", end="")
                현재노드 = 현재노드.prev
            print(f"(head : {self.count} 노드)")

    # 리스트의 맨뒤에 새노드(newNode)를 연결한다.
    def append(self,value):
        newNode = Node(value)
        # 빈 리스트에 처음 추가하는 상황이면
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
        else:
            # 리스트의 마지막 노드(tail)뒤에 연결한다
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.count+=1

    # 리스트 맨 앞에 새노트 추가한다.
    def insert(self, value):
        newNode = Node(value)
        # 빈리스트인 경우 별도 처리
        if self.count == 0:
            self.append(value)
        # 나머지는 일반적인 경우
        else:
             newNode.next = self.head
             self.head.prev = newNode
             self.head = newNode
             self.count += 1

    # 리스트 의 target 노드 앞에 새 노드를 추가 한다.
    def insertBefore(self, target, value):
        # target이 head인경우
        if target == self.head:
            self.insert(value)
        # target 앞에 다른 노드가 있는 경우
        else:
            newNode = Node(value)
            newNode.next = target
            newNode.prev = target.prev
            target.prev.next = newNode
            target.prev = newNode
            self.count += 1

    # target 노드뒤에 새노드 삽입하기
    def insertAfter(self, target, value):
        if target == self.tail:
            self.append(value)
        else:
            newNode = Node(value)
            newNode.next = target.next
            newNode.prev = target
            target.next.prev = newNode.next
            target.next = newNode
            self.count+=1

    # 주어진 값과 일치하는 노드를 찻아 변환하기 없으면 None 변환
    def find(self, value):
        currentNode = self.head
        while currentNode != None:
            if currentNode.data == value: # 찻았으면 currentNode 변환
                return currentNode
            else:
                currentNode = currentNode.next
        return None

    # 주어진 노드를 리스트애서 제거하기
    def remove(self, targetNode):
        if targetNode == None:
            return 0
        # 리스트 에 노드가 1개뿐이면 (heard == tail)
        # Dlist 의 속성 hard tail 정보를 None 으로 처리하는 것이 중요.
        if self.count == 1:
            self.head = None
            self.tail = None
        elif targetNode == self.head:
            self.head = targetNode.next
            targetNode.next.prev = None
        elif targetNode == self.tail:
            targetNode.prev.next = None
            self.tail = targetNode.prev
        else:
            targetNode.prev.next = targetNode.next
            targetNode.next.prev = targetNode.prev

        del targetNode
        self.count -= 1

     # 노드의 정렬 상대를 오름차순츠으로 유지하면서 추가하기
     # 오름차순으로 정렬 유지하면서 이메소드만으로 노드를 추가하여야함
    def insertSorted(self, value):
        if self.count == 0:
            self.append(value)
            return
        # 노드가 1개이상인 경우에는 새노드에 위치가 정렬되는 위치에 추가
        currentNode = self.head
        while currentNode != None:
            if value < currentNode.data:
                self.insertBefore(currentNode, value)
                return
            currentNode = currentNode.next
        # 여기까지 왔으면 newNode 가 가장큰 값이므로 append 시
        self.append(value)

    def isEmpty(self):
        return self.count == 0

# ====================================================================================================================================================================================================
# error exception class(프로그램 중단)
class StackUnderFlow(Exception):
    pass

class QueueUnderFlow(Exception):
    pass


# ====================================================================================================================================================================================================
# Class DList를 상속하여 stack class를 정의한다.
# class stack은 부모클래스 DList 속성 매소드를 뮬러받고.
# 다른 속성,메소드를 추가할수있다
class Stack(DList):
    def push(self, value):
        self.insert(value)

    # 스택의 제일 위에 있는 값을 제거한다
    # 값을 제거하면서 제거되는값을 반환한다.
    def pop(self):
        if self.count == 0:
            raise StackUnderFlow("stack empty!!!")
        else:
            returnvalue = self.head.data
            self.remove(self.head)
            return returnvalue

    # 스택에 top에 잇는 값만 확인
    def peek(self):
        if self.count == 0:
            raise StackUnderFlow("stack empty!!!")
        else:
            return self.head.data

#===================================================================================================
#class Queue
# 이중연결라스트 Dlist를 상속받아서 구현한다
class Queue(DList):
    def add(self,value):
        self.append(value)

    def remove(self):
        if self.isEmpty():
            raise QueueUnderFlow("Queue is Empty!!")
        else:
            retvalue = self.head.data
            super().remove(self.head)
            return retvalue




























