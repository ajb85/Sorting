# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):    
    merged = []
    i = 0
    j = 0

    while i < len(arrA) or j < len(arrB):
        if(j == len(arrB)):
            merged.append(arrA[i])
            i += 1
        elif(i == len(arrA)):
            merged.append(arrB[j])
            j += 1
        elif(arrA[i] <= arrB[j]):
            merged.append(arrA[i])
            i += 1
        elif(arrB[j] <= arrA[i]):
            merged.append(arrB[j])
            j += 1
        else:
            print("ruh roh, something unexpected happened: ", f"{arrA[i]} {arrB[j]}")
    
    return merged

print(merge([1,2,3], [4,5,6,7]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

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
def timsort( arr ):

    return arr
