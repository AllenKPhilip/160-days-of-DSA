"""
Author:ALLEN K PHILIP
Description:an array of integers arr[]. Your task is to reverse the given array.
"""
def reverseArray(arr):
    arr.reverse()
    return arr
  
if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverseArray(arr)
  
    for i in range(len(arr)):
        print(arr[i], end=" ")
