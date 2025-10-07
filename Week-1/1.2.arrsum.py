from typing import List

def arrsum(n: int, S: List[int]) -> int:
    # Complete the code here
    sum = 0
    for i in range(n):
        sum += S[i]
    return sum
