class node(object):
    def __init__(self, v):
        self.val = v
        self.next = None

def createLink(l):
    h = node(0)
    head = h
    for i in l:
        m = node(i)
        head.next = m
        head = head.next
    return h.next


#3-2
def reverse(head):
    pre = None
    while head!=None:
        tmp = head.next
        head.next = pre
        pre = head
        head = tmp
    return pre


#3-20
def findMid(head):
    if head==None:
        return None
    h = head
    count = 0
    while head!=None:
        count+=1
        head = head.next
    if count%2 == 1:
        mid = (count-1)//2
    else:
        mid = count//2 - 1
    for i in range(mid):
        h = h.next
    return h.val


if __name__=="__main__":
    l = [1,2,3,4,5,6,7]
    # 3-3
    head = createLink(l)
    h = head
    # Original
    while head!=None:
        print(head.val)
        head = head.next

    #reverse
    new_head = reverse(h)
    print("Reverse")

    # new one
    while new_head!=None:
        print(new_head.val)
        new_head = new_head.next

    # 3-20
    h0 = createLink([1])
    h1 = createLink([1,2,3])
    h2 = createLink([1,2,3,4,5,6])
    r0 = findMid(h0)
    r1 = findMid(h1)
    r2 = findMid(h2)
    print("mid of r0 is "+ str(r0))
    print("mid of r1 is " + str(r1))
    print("mid of r2 is " + str(r2))


