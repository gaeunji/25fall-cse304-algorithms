from typing import List

# Global variable type declarations
n: int
W: float
w: List[float]
p: List[float]
maxprofit: float
bestset: List[bool]
include: List[bool]

def promising(i: int, weight: float, profit: float) -> bool:
    global n, W, w, p, maxprofit
    # Complete the code here
    if weight >= W:
        return False
    else: # 무게 초과가 아닌 경우 -> 나머지 아이템들을 넣었을 때의 bound 계산
        bound = profit
        j = i + 1
        totweight = weight
        while j <= n and totweight + w[j] <= W:
            totweight += w[j]
            bound = bound + p[j]
            j += 1
        k = j
        if k <= n:
            bound = bound + (W - totweight) * p[k] / w[k]

    return bound > maxprofit

def knapsack(i: int, weight: float, profit: float) -> None:
    global n, W, w, p, bestset, include, maxprofit
    if weight <= W and profit > maxprofit:
        # Complete the code here
        maxprofit = profit
        bestset = include[:]
    if promising(i, weight, profit): # 다음 물건에 대해 포함하거나 포함하지 않거나 두 가지 경우 고려
        # Complete the code here
        include [i + 1] = True
        knapsack(i+1, weight + w[i+1], profit + p[i+1])
        include [i + 1] = False
        knapsack(i+1, weight, profit)
    return 