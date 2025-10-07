from typing import List

def partition(low: int, high: int, S: List[int]) -> int:
    pivotitem = S[low]
    j = low # 피벗의 위치

    # Complete the code here
    for i in range(low+1, high+1):
        if S[i] < pivotitem:
            j += 1 # 작은 항목을 발견하면 1 늘린다
            S[i], S[j] = S[j], S[i]
    S[low], S[j] = S[j], S[low] # pivotitem 값을 pivotpoint로 이동 
    return j


def quicksort(low: int, high: int, S: List[int]) -> None:
    if low < high:
        # Complete the code here
        pivot = partition(low, high, S)
        quicksort(low, pivot-1, S)
        quicksort(pivot+1, high, S)