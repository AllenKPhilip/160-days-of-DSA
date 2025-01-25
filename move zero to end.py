"""
Author:ALLEN K PHILIP
Description:given an array arr[] of non-negative integers. Your task is to move all the zeros
in the array to the right end while maintaining the relative order of the non-zero elements.
"""
def pushZerosToEnd(arr):
    n = len(arr)
    temp = [0] * n  
    j = 0

    for i in range(n):
        if arr[i] != 0:
            temp[j] = arr[i]
            j += 1

    while j < n:
        temp[j] = 0
        j += 1

    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)

    for num in arr:
        print(num, end=" ")
