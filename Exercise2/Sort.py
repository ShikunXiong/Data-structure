import Exercise2.ProcessFile as pf
import time
import sys
sys.setrecursionlimit(2000000)

# 选择排序
def selectionsort(list):
    start = time.clock()
    size = len(list)
    for i in range(size-1):
        for j in range(i+1, size):
            if list[j]<list[i]:
                list[i], list[j] = list[j], list[i]
    end = time.clock()
    return end-start, list

#插入排序
def insertsort(list):
    start = time.clock()
    size = len(list)
    for i in range(1, size):
        key = list[i]
        j = i-1
        while j>=0 and key<list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    end = time.clock()
    return end-start, list

#堆排序
def heapify(list, size, i):
    large = i
    left = 2*i + 1
    right = 2*i + 2
    if left<size and list[i]<list[left]:
        large = left
    if right<size and list[large]<list[right]:
        large = right
    if large!=i:
        list[i], list[large] = list[large], list[i]
        heapify(list, size, large)

def heapsort(list):
    start = time.clock()
    size = len(list)
    for i in range(size, -1, -1):
        heapify(list, size, i)
    for i in range(size-1, 0, -1):
        list[0], list[i] = list[i], list[0]
        heapify(list, i, 0)
    end = time.clock()
    return end-start, list

#归并排序
def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

def mergesort(list):
    start = time.clock()
    if len(list) <= 1:
        return list
    num = len(list) // 2
    left = mergesort(list[:num])
    right = mergesort(list[num:])
    end = time.clock()
    return end-start, merge(left, right)

#快速排序
def qsort(left, right, nums):
    start = time.clock()
    if left < right:
        mid = quicksort(left, right, nums)
        qsort(left, mid - 1, nums)
        qsort(mid + 1, right, nums)
    end = time.clock()
    return end-start, nums

def quicksort(left, right, nums):
    refer = nums[left]
    while left < right:
        while left < right and nums[right] >= refer:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= refer:
            left += 1
        nums[right] = nums[left]
    nums[left] = refer
    return left


if __name__ == "__main__":
    f = open("pride-and-prejudice.txt", mode='r', encoding='utf-8-sig')
    list = []
    # get list
    for line in f.readlines():
        line.strip("\n")
        list += pf.processLine(line)
    # sort
    t, s = selectionsort(list)
    print("time: " + str(t) + "\n")
    f.close()

"""
quick 3.303799
heap 1.538304
insert 1133.847481
select 
"""