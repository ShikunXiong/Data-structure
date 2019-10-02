import Exercise1.LinkedListSet as ll
import Exercise1.ProcessFile as pf
import time

class hashSet:
    def __init__(self):
        self.hashmap = [None]*300

    def contains(self, word):
        index = abs(hash(word)) % 300
        link = self.hashmap[index]
        if link is None:
            return False
        return link.contains(word)

    def add(self, word, w):
        start = time.clock()
        if self.contains(word) is False:
            index = abs(hash(word)) % 300
            link = self.hashmap[index]
            if link is None:
                node = ll.Node(word)
                link = ll.LinkedList(node)
                self.hashmap[index] = link
            else:
                link.addHashNode(word)
            end = time.clock()
            w.write(str(self.size() - 1) + "," + str(end - start) + "\n")
            return True

        else:
            return False

    def size(self):
        l = 0
        count = 0
        h = self.hashmap
        for link in h:
            if link is not None:
                l += 1
                count += link.size()
        return count

def testSet():
    f = open("pride-and-prejudice.txt", mode='r', encoding='utf-8-sig')
    w = open("HashInsertTime.csv", 'a', encoding='utf-8')
    hashset = hashSet()
    for line in f.readlines():
        line = line.strip("\n")
        arr = pf.processLine(line)
        for item in arr:
            if item != " " and item:
                hashset.add(item, w)
    a = 1
    return hashset

def compare(Hashset):
    f = open("words-shuffled.txt", mode='r', encoding='utf-8-sig')
    count = 0
    for line in f.readlines():
        line = line.strip("\n")
        if Hashset.contains(line) == False:
            print(line)
            count += 1
    f.close()
    return count