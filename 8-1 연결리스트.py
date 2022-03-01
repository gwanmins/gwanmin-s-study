class Node :
    def __init__(self, data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        init=Node('init')
        self.head=init
        self.tail=init

        self.현재노드=None
        self.데이터수=0

    def append(self, data):
        새로운노드=Node(data)
        self.tail.next= 새로운노드
        self.tail=새로운노드
        self.데이터수 += 1

a=linkedlist()
a.append(int(input("입력")))
b=a[::-1]

if a==b :
    print(true)

else :
    print(false)
