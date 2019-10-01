#4-5
def findMost(l):
    dic = {}
    max = 0
    result = []
    for i in l:
        dic.setdefault(i, 0)
        dic[i]+=1
        if dic[i]>max:
            max = dic[i]
            result = [i]
        elif dic[i]==max:
            result.append(i)
    return result

#4-16
def findMedianOdd(l, start, end):
    mid  = quicksort(l, start, end)
    length = len(l)
    if start<end:
        median = length//2
        if mid==median:
            return l[mid]
        elif mid>median:
            return findMedianOdd(l, start, mid-1)
        else:
            return findMedianOdd(l, mid+1, end)
    return l[mid]

def findMedianEven(l, start, end, f1, f2, m1, m2):
    mid  = quicksort(l, start, end)
    if start<end:
        if mid==m1:
            if f2==True:
                return (l[m1]+l[m2])/2
            f1 = True
            return findMedianEven(l, mid+1, end, f1, f2, m1, m2)
        elif mid==m2:
            if f1==True:
                return (l[m1]+l[m2])/2
            f2 = True
            return findMedianEven(l, start, mid-1, f1, f2, m1, m2)
        elif mid<m1:
            return findMedianEven(l, mid+1, end, f1, f2, m1, m2)
        elif mid>m2:
            return findMedianEven(l, start, mid-1, f1, f2, m1, m2)
    return (l[m1]+l[m2])/2


def quicksort(arr, start, end):
    ref = arr[start]
    while start<end:
        while start<end and arr[end]>=ref:
            end-=1
        arr[start] = arr[end]
        while start<end and arr[start]<=ref:
            start+=1
        arr[end] = arr[start]
    arr[start] = ref
    return start



if __name__=="__main__":
    # 4-5
    l = [4,6,2,4,3,1,3]
    r = findMost(l)

    # 4-16
    arr = [1,2,3,4]
    if len(arr)%2==1:
        result = findMedianOdd(arr, 0, len(arr)-1)
    else:
        m2 = len(arr)//2
        m1 = len(arr)//2 - 1
        result = findMedianEven(arr, 0, len(arr)-1, False, False, m1, m2)
    print(result)
