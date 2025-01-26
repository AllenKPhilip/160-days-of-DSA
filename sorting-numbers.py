"""
Author:ALLEN K PHILIP
Description:an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
"""

def sort012(arr):
    c0 = 0
    c1 = 0
    c2 = 0

    for num in arr:
        if num == 0:
            c0 += 1
        elif num == 1:
            c1 += 1
        else:
            c2 += 1

    idx = 0
