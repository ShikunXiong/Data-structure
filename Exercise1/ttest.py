import Exercise1.BinSet as b
if __name__ == "__main__":
    n = b.BinNode(0)
    root = b.binset(n)
    root.add(1)
    root.add(2)
    root.add(3)
    root.add(4)
    print(root.count)