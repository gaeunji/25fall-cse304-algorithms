from typing import List

def seqsearch(n: int, S: List[int], x: int) -> int: 
    location = 0

    # Complete the code here
    while location < n and S[location] != x:
        location += 1
    if location == n: # 배열의 끝까지 탐색했는데 찾지 못했을 경우
        location = -1
    return location