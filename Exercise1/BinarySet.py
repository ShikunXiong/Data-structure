import time
import Exercise1.ProcessFile as pf

class BinNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class BinSet:
    def __init__(self, root):
        self.head = root

    def add(self, word, w):
        p = self.head
        start = time.clock()
        if self.contains(word) == False:
            n = BinNode(word)
            n.next = self.head
            self.head = n
            end = time.clock()
            w.write(str(self.size()-1) + "," + str(end-start) + "\n")
            return True
        else:
            return False

    def contains(self, word):
        p = self.head
        while p is not None:
            if p.val == word:
                return True
            p = p.next
        return False

    def size(self):
        count = 0
        p = self.head
        while p != None:
            p = p.next
            count += 1
        return count

def testBin():
    f = open("pride-and-prejudice.txt", encoding='utf-8-sig')
    w = open("BinInsertTime.csv", 'a', encoding='utf-8')
    hasHead = False
    for line in f.readlines():
        line = line.strip("\n")
        arr = pf.processLine(line)
        for item in arr:
            if item != " " and item:
                if hasHead == False:
                    hasHead = True
                    node = BinNode(item)
                    Binset = BinSet(node)
                if Binset.contains(item) == False:
                    Binset.add(item, w)
    return Binset

def compare(Binset):
    f = open("words-shuffled.txt", encoding='utf-8-sig')
    count = 0
    for line in f.readlines():
        line = line.strip("\n")
        if Binset.contains(line) == False:
            count += 1
    return count
