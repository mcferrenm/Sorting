# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # [3] [5]
    # [3] [5, 6]
    # [3, 0, 0]
    #
    idxA = 0
    idxB = 0
    for i in range(0, len(merged_arr)):
        if len(arrA) - 1 < idxA:
            merged_arr[i] = arrB[idxB]
            idxB += 1
        elif len(arrB) - 1 < idxB:
            merged_arr[i] = arrA[idxA]
            idxA += 1
        elif arrA[idxA] < arrB[idxB]:
            merged_arr[i] = arrA[idxA]
            idxA += 1
        else:
            merged_arr[i] = arrB[idxB]
            idxB += 1
    return merged_arr

    #


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)
    return arr


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


# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled
