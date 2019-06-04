import math

# TO-DO: complete the helper function below to merge 2 sorted arrays

# def merge( arrA, arrB ):    

# I wrote this before starting the problem.  It sorts 2 random arrays pretty well but that's not how I
# ended up solving the problem.  So it's here, but doesn't work with my solution

#     merged = []
#     i = 0
#     j = 0
#     print("arrA: ", arrA, "arrB: ", arrB)
#     while i < len(arrA) or j < len(arrB):
#         if(j >= len(arrB)):
#             print("max j, merging: ", arrA[i])
#             merged.append(arrA[i])
#             i += 1
#         elif(i >= len(arrA)):
#             print("max i, merging: ", arrB[j])
#             merged.append(arrB[j])
#             j += 1
#         elif(arrA[i] <= arrB[j]):
#             print("a < b, merging: ", arrA[i])
#             merged.append(arrA[i])
#             i += 1
#         elif(arrB[j] <= arrA[i]):
#             print("b < a, merging: ", arrB[j])
#             merged.append(arrB[j])
#             j += 1
#         else:
#             print("ruh roh, something unexpected happened: ", f"{arrA[i]} {arrB[j]}")
    
#     return merged

def merge(sorted, split):
    if(len(split) == 0):
        return sorted
        
    item = split.pop(0)[0] 
    if(len(sorted) == 0 or sorted[len(sorted)-1] <= item):
        sorted.append(item)
    else:
        for i in range(len(sorted)):
            if sorted[i] >= item:
                sorted.insert(i,item)
                break

    return merge(sorted, split)
    



def split_array(arr):
    if(len(arr)<=1):
        return [arr]
    half = math.ceil(len(arr)/2)

    return split_array(arr[half:]) + split_array(arr[:half])



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    split = split_array(arr)
    sorted = merge([], split)

    return sorted

print(merge_sort([1,21,13,4,55,16,5,8,9]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
