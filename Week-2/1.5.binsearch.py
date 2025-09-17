# name: 
# student id: 
from typing import List

def binsearch(n: int, S: List[int], x: int) -> int:
    low, high = 0, n - 1
    location = -1

    # Complete the code here
    for i in range(n):
        mid = (low + high) // 2
        if S[mid] == x:
            location = mid
            break
        elif S[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return location