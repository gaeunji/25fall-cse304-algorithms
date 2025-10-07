from typing import List

def exchangesort(n: int, S: List[int]) -> None:
    # Complete the code here
    for i in range(n-1):
        for j in range(i+1, n):
            if S[i] > S[j]:
                S[i], S[j] = S[j], S[i]