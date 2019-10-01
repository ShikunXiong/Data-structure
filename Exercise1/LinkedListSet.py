import time
import Exercise1.ProcessFile as pf


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head

    def add(self, word, w):
        start = time.clock()
        if self.contains(word) == False:
            n = Node(word)
            n.next = self.head
            self.head = n
            end = time.clock()
            w.write(str(self.size()-1) + "," + str(end-start) + "\n")
            return True
        else:
            return False

    def addHashNode(self, word):
        node = Node(word)
        node.next = self.head
        self.head = node
        m = 1

    def contains(self, word):
        p = self.head
        while p is not None:
            if p.val == word:
                return True
            p = p.next
            a = self.head
            t = 1
        return False

    def size(self):
        count = 0
        p = self.head
        while p != None:
            p = p.next
            count += 1
        return count

def testLinked():
    f = open("pride-and-prejudice.txt", mode='r', encoding='utf-8-sig')
    w = open("LinkInsertTime.csv", 'a', encoding='utf-8')
    hasHead = False
    for line in f.readlines():
        line = line.strip("\n")
        arr = pf.processLine(line)
        for item in arr:
            if item != " " and item:
                if hasHead == False:
                    hasHead = True
                    node = Node(item)
                    link = LinkedList(node)
                if link.contains(item) == False:
                    link.add(item, w)
    f.close()
    w.close()
    return link

def compare(link):
    f = open("words-shuffled.txt", mode='r', encoding='utf-8-sig')
    count = 0
    for line in f.readlines():
        line = line.strip("\n")
        if link.contains(line) == False:
            count += 1
    f.close()
    return count


