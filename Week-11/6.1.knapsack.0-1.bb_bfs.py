from typing import List

class Node:
    def __init__(self, level, weight, profit):
        self.level = level
        self.weight = weight
        self.profit = profit

def boundof(u: Node, n: int, W: float, w: List[float], p: List[float]) -> float:
    if u.weight >= W:
        return 0
    else:
        # Complete the code here
        result = u.profit
        j = u.level + 1
        totweight = u.weight
        while j <= n and totweight + w[j] <= W:
            totweight += w[j]
            result += p[j]
            j += 1
        k = j
        if k <= n and w[k] > 0:
            result += (W - totweight) * p[k] / w[k]
        return result

def knapsack2(n: int, W: float, w: List[float], p: List[float]) -> float:
    count = 0
    queue = [] # Initialize Queue
    v = Node(0, 0, 0)
    v.bound = boundof(v, n, W, w, p)
    maxprofit = 0
    queue.append(v)
    count+=1
    while len(queue) != 0:
        # Complete the code here
        u = queue.pop(0)
        if u.bound > maxprofit:
            if u.level < n:
                # Include the next item
                if u.weight + w[u.level + 1] <= W:
                    v = Node(u.level + 1, u.weight + w[u.level + 1], u.profit + p[u.level + 1])
                    v.bound = boundof(v, n, W, w, p)
                    if v.bound > maxprofit:
                        queue.append(v)
                    if v.profit > maxprofit:
                        maxprofit = v.profit
                # Exclude the next item
                v = Node(u.level + 1, u.weight, u.profit)
                v.bound = boundof(v, n, W, w, p)
                if v.bound > maxprofit:
                    queue.append(v)
                if v.profit > maxprofit:
                    maxprofit = v.profit
            else:
                # Leaf node, update maxprofit if needed
                if u.profit > maxprofit:
                    maxprofit = u.profit
        count += 1
    return maxprofit
