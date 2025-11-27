from typing import List

def insertionsort(n: int, S: List[int]) -> None:
    # Complete the code here
    for i in range(1, n):
        key = S[i]
        j = i - 1
        while j >= 0 and S[j] > key:
            S[j + 1] = S[j]
            j = j - 1
        S[j + 1] = key
    return S