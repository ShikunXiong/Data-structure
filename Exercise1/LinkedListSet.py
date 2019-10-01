import Exercise1.ProcessFile as pf

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head

    def add(self, str):
        p = self.head
        while p is not None:
            if p.val == str:
                return False
            else:
                p=p.next
        n = Node(str)
        n.next = self.head
        self.head = n
        return True

    def contains(self, str):
        p = self.head
        while p is not None:
            if p.val == str:
                return True
            p = p.next
        return False

    def size(self):
        count = 0
        p = self.head
        while p != None:
            p = p.next
            count+=1
        return count

def testLinked():
    f = open("pride-and-prejudice.txt", encoding='utf-8-sig')
    hasHead = False
    for line in f.readlines():
        line = line.strip("\n")
        arr = pf.processLine(line)
        print(arr)
        for item in arr:
            if item != " " and item:
                if hasHead == False:
                    hasHead = True
                    node = Node(item)
                    link = LinkedList(node)
                if link.contains(item) == False:
                    link.add(item)
    print(link.size())


