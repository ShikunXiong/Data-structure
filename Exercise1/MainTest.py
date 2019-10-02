import Exercise1.LinkedListSet as ll
import Exercise1.BinarySet as bs
import Exercise1.HashSet as hs

if __name__ == "__main__":


    link = ll.testLinked()
    num_miss_1 = ll.compare(link)
    print("size1 = " + str(link.size()))
    print("miss1 = " + str(num_miss_1))

    """
    Binset = bs.testBin()
    num_miss_2 = bs.compare(Binset)
    print("size2 = " + str(Binset.size()))
    print("miss2 = " + str(num_miss_2))
    """

    """
    hashset = hs.testSet()
    num_miss_3 = hs.compare(hashset)
    print("size3 = " + str(hashset.size()))
    print("miss3 = " + str(num_miss_3))
    """