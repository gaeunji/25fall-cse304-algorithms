from heapq import heappush, heappop
from typing import List

class Node:
    def __init__(self, level, weight, profit):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = 0

def boundof(u: Node, n: int, W: float, w: List[float], p: List[float]) -> float:
    if u.weight >= W:
        return 0
    else:
        # Complete the code here
        result = u.profit
        totweight = u.weight
        k = u.level + 1
        
        # 남은 용량만큼 아이템을 greedy하게 추가
        while k <= n and totweight + w[k] <= W:
            totweight += w[k]
            result += p[k]
            k += 1
        
        # 마지막 아이템은 분할해서 추가 
        if k <= n and w[k] > 0:
            result += (W - totweight) * (p[k] / w[k])
        
        return result

def knapsack3(n: int, W: float, w: List[float], p: List[float]) -> float:
    count = 0
    heap = [] # Initialize Priority Queue
    v = Node(0, 0, 0)
    v.bound = boundof(v, n, W, w, p)
    maxprofit = 0
    heappush(heap, (-v.bound, count, v))
    count +=1
    while len(heap) != 0:
        # 최고우선검색(Best-First Search) 전략
        # 1. 주어진 노드의 모든 자식 노드를 검색한 후,
        # 2. 유망하면서 확장되지 않은(unexpanded) 노드를 살펴보고,
        # 3. 그 중에서 가장 좋은 한계치(bound)를 가진 노드를 확장한다
        # Complete the code here
        _, _, v = heappop(heap)
        
        # 유망한 노드만 확장
        if v.bound > maxprofit and v.level < n:
            # 왼쪽 자식 노드 (아이템을 포함하는 경우)
            if v.weight + w[v.level + 1] <= W:
                u = Node(v.level + 1, v.weight + w[v.level + 1], v.profit + p[v.level + 1])
                
                # 최대 이익 갱신
                if u.profit > maxprofit:
                    maxprofit = u.profit
                
                # 한계치 계산 및 유망하면 큐에 추가
                u.bound = boundof(u, n, W, w, p)
                if u.bound > maxprofit:
                    heappush(heap, (-u.bound, count, u))
                    count += 1
            
            # 오른쪽 자식 노드 (아이템을 포함하지 않는 경우)
            u = Node(v.level + 1, v.weight, v.profit)
            
            # 한계치 계산 및 유망하면 큐에 추가
            u.bound = boundof(u, n, W, w, p)
            if u.bound > maxprofit:
                heappush(heap, (-u.bound, count, u))
                count += 1
        elif v.level == n:
            # Leaf node, update maxprofit if needed
            if v.profit > maxprofit:
                maxprofit = v.profit

    return maxprofit
