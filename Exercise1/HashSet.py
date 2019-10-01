import Exercise1.LinkedListSet as ll
import Exercise1.ProcessFile as pf

class hashSet:
    def __init__(self):
        self.hashmap = [None]*2

    def contains(self, word):
        index = abs(hash(word)) % 2
        link = self.hashmap[index]
        if link is None:
            return False
        return link.contains(word)

    def add(self, word):
        if self.contains(word) is False:
            index = abs(hash(word)) % 2
            link = self.hashmap[index]
            a = word
            if link is None:
                m = 1
                print("link is none")
                node = ll.Node(word)
                link = ll.LinkedList(node)
                m = 1
                self.hashmap[index] = link
                m = 1
            else:
                print('link exists')
                m = 1
                link.addHashNode(word)
            return True
        else:
            print('already there')
            return False

    def size(self):
        l = 0
        count = 0
        h = self.hashmap
        for link in h:
            if link is not None:
                l += 1
                count += link.size()
        print("有多少链表" + str(l))
        return count

def testSet():
    f = open("pride-and-prejudice.txt", mode='r', encoding='utf-8-sig')
    hashset = hashSet()
    for line in f.readlines():
        line = line.strip("\n")
        arr = pf.processLine(line)
        for item in arr:
            if item != " " and item:
                hashset.add(item)
    a = 1
    print(hashset.size())
    return hashset

