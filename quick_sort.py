from random import shuffle

lst = [i for i in range(10)]
length = len (lst)
shuffle(lst)
print(lst)

def quick_sort(list_, low, high):
    if low<high:
        pivot = low
        i = low
        j = high
        while i < j :
            while list_[i] <= list_[pivot] and i < high:
                i +=1
            while list_[j]>list_[pivot]:
                j -=1
            if i<j:
                list_[i], list_[j] = list_[j],list_[i]
        list_[j], list_[pivot] = list_[pivot], list_[j]


        quick_sort(list_, low,j -1)
        quick_sort(list_, j+ 1, high)

    return list_

print(quick_sort(lst,0,length-1))
