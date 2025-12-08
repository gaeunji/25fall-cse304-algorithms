from heapq import heappush, heappop
from typing import List, Tuple
import time

INF = float("inf")

class Node:
    def __init__(self, level, path):
        self.level = level
        self.path = path[:]
        self.bound = 0

def remainder(path: List[int], n: int) -> int:
    return n * (n + 1) // 2 - sum(path)

def pathlength(path: List[int], W: List[List[float]]) -> float:
    # Complete the code here
    length = 0
    for i in range(len(path) - 1):
        length += W[path[i]][path[i + 1]]

    return length

def hasOutgoing(v: int, path: List[int]) -> bool:
    return v in path[:len(path)-1]

def hasIncoming(v: int, path: List[int]) -> bool:
    return v in path[1:]

def boundof(v: Node, n: int, W: List[List[float]]) -> float:
    global INF
    lower = pathlength(v.path, W)
    for i in range(1, n + 1):
        # Complete the code here
        # i에서 나가는 간선이 아직 사용되지 않은 경우
        if not hasOutgoing(i, v.path):
            min_out = INF
            for j in range(1, n + 1):
                if i != j and W[i][j] < min_out:
                    min_out = W[i][j]
            if min_out < INF:
                lower += min_out
        
        # i로 들어오는 간선이 아직 사용되지 않은 경우
        if not hasIncoming(i, v.path):
            min_in = INF
            for j in range(1, n + 1):
                if i != j and W[j][i] < min_in:
                    min_in = W[j][i]
            if min_in < INF:
                lower += min_in
        lower = lower / 2

    return lower

def travel2(n: int, W: List[List[float]]) -> Tuple[float, List[int]]:
    global INF
    heap = [] # Initialize Priority Queue
    v = Node(0, [1])
    v.bound = boundof(v, n, W)
    minlength, opttour = INF, []
    heappush(heap, (v.bound, time.time(), v))
    while len(heap) != 0:
        v = heappop(heap)[2]
        if v.bound < minlength:
            for i in range(2, n + 1):
                # Complete the code here
                if i not in v.path:
                    u = Node(v.level + 1, v.path + [i])
                    
                    # 모든 정점을 방문한 경우
                    if u.level == n - 1:
                        # 시작점으로 돌아가는 경로 추가
                        u.path.append(1)
                        length = pathlength(u.path, W)
                        
                        # 최소 길이 갱신
                        if length < minlength:
                            minlength = length
                            opttour = u.path[:]
                    else:
                        # 아직 방문할 정점이 남은 경우
                        u.bound = boundof(u, n, W)
                        
                        # 유망한 노드만 큐에 추가
                        if u.bound < minlength:
                            heappush(heap, (u.bound, time.time(), u))
                
    return minlength, opttour
