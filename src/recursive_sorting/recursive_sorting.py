# TO-DO: complete the helpe function below to merge 2 sorted arrays

def merge(arrA, arrB):
    # TO-DO
    merged_arr = []
    while len(arrA) != 0 and len(arrB) != 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])
        else:
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])
    if len(arrA) == 0:
        merged_arr += arrB
    else:
        merged_arr += arrA
    return merged_arr

print(merge([100432, 5434, 7433], [9453, 8554, 3453]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else: 
        sort_index = len(arr)// 2
        left = merge_sort(arr[:sort_index])
        right = merge_sort(arr[sort_index:])
        return merge(left, right)

print(merge_sort([9453, 8554, 3453, 100432, 5434, 7433]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
