import Exercise1.ProcessFile as pf

class BinNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class binset:
    def __init__(self, root):
        self.root = root
        self.now = [self.root]
        self.count = 1

    def contains(self, root, word):
        if root is None:
            return False
        if root.val == word:
            return True
        else:
            f1 = self.contains(root.left, word)
            f2 = self.contains(root.right, word)
        return f1 or f2

    def add(self, word):
        if self.contains(self.root, word):
            return False
        n = self.now[0]
        if n.left is None:
            t = BinNode(word)
            n.left = t
            self.now.append(t)
        elif n.right is None:
            t = BinNode(word)
            n.right = t
            self.now.append(t)
            self.now.pop(0)
        self.count += 1
        return True

    def size(self):
        return self.count

def testBin():
    f = open("pride-and-prejudice.txt", encoding='utf-8-sig')
    hasRoot = False
    for line in f.readlines():
        line = line.strip("\n")
        arr = pf.processLine(line)
        for item in arr:
            if item != " " and item:
                if hasRoot == False:
                    hasRoot = True
                    node = BinNode(item)
                    root = binset(node)
                root.add(item)
    return root

def compare(binset):
    f = open("words-shuffled.txt", encoding='utf-8-sig')
    count = 0
    for line in f.readlines():
        line = line.strip("\n")
        if binset.contains(line) == False:
            count += 1
    return count