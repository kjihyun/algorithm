class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

## enqueue (data) 맨위에 데이터 추가하기
## dequeue() 맨위 데이터 뽑기
##peek 맨위 데이터 보기



class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # head    tail
    ##[4] --> [3}

    #head         tail
    # [4] -> [3]->[2]

    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head= new_node
            self.tail=new_node
            return
        self.tail.next= new_node
        new_node = self.tail


#head      tail
#[4]->[2]->[3]
#head  tail
#[2]->[3]
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        delete_node=self.head
        self.head= self.head.next

        return delete_node.data

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.head.data

    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None



queue=Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
