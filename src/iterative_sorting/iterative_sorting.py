# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # cur_index = i
        # smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr) - 1):
            if arr[i] > arr[j + 1]:
                # TO-DO: swap
                arr[i], arr[j + 1] = arr[j + 1], arr[i]

    return arr


# print(selection_sort([0, 1, 10, 3, 4, 5, 6, 8, 9, 7]))
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    i = 0
    swaped = True
    while swaped | i < len(arr) - 1:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swaped = True
            i = 0
            continue
        else:
            swaped = False
        i += 1
    return arr

# def bubble_sort(arr):
#     swapped = True  # O(1)
#     while swapped is True:  # O(n)
#         swapped = False  # O(1)
#         print(arr)
#         for i in range(1, len(arr)):  # O(n)
#             if arr[i - 1] > arr[i]:  # O(1)
#                 temp = arr[i]  # O(1)
#                 arr[i] = arr[i-1]  # O(1)
#                 arr[i-1] = temp  # O(1)
#                 swapped = True  # O(1)
#         print(swapped)
#     return arr

print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
