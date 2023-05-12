from NodesList import Node
from NodesList import SList

# 단순 연결 라스트 생성
sl = SList() #노드는 아직없는 빈리스트 생성

#위에서 생성한 리스트에서 노드 추가하여 연결하기
sl.printList()
sl.insertFront(100)
sl.printList()
sl.insertFront(200)
sl.printList()
sl.append(300)
sl.printList()
sl.insertBefore(50, Node(50))









