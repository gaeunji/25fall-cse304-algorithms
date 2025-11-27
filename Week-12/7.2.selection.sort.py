from typing import List

def selectionsort(n: int, S: List[int]) -> None:
    # Complete the code here
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if S[j] < S[min_index]:
                min_index = j
        S[i], S[min_index] = S[min_index], S[i]
    return S