# nums_bs = [5, 6, 2, 1, 3, 4]
# nums_sels = [5, 6, 2, 1, 3, 4]
# nums_is=[5, 6, 2, 1, 3, 4]
# print(nums_bs)
# print(nums_sels)
# print(nums_is)

def buble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True
    return ls

# print(buble_sort(nums_bs))
# print(nums_bs)


def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]
    return ls


# selection_sort(nums_sels)
# print(nums_sels)

def insertion_sort(ls):
    for i in range(1,len(ls)):
        key=ls[i]
        j = i -1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
            ls[j+1]=key
        return ls

# insertion_sort(nums_is)
# print(nums_is)