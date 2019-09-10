# TO-DO: complete the helpe function below to merge 2 sorted arrays

def merge(arrA, arrB):
    # TO-DO
    merged_arr = []
    # when the length of the param lists are not 0...
    while len(arrA) != 0 and len(arrB) != 0:
        # if the first value of list A is smaller than the first of list B...
        if arrA[0] < arrB[0]:
            # add the list A value to the merged list and remove it from its native list
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])
        else:
            # else add the list B value to the merged list and remove it from its native list
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])
    # if the length of list A is 0, combine merged list and list B
    if len(arrA) == 0:
        merged_arr += arrB
    # else combine merged list and list A
    else:
        merged_arr += arrA
    return merged_arr

print(merge([100432, 5434, 7433], [9453, 8554, 3453]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # if the length of the param list is smaller than or equal to 1, return the list
    if len(arr) <= 1:
        return arr
    #else ...
    else: 
        # middle number is the length of param list divided by 2 (no float)
        sort_index = len(arr)// 2
        # separate list on either side of middle
        left = merge_sort(arr[:sort_index])
        right = merge_sort(arr[sort_index:])
        # merge using merge helper
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
