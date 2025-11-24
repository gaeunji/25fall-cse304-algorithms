from typing import List

# Global variables
W: List[List[int]] = []     # Adjacency matrix
vcolor: List[int] = []      # Vertex colors
n: int = 0                  # Number of vertices
count: int = 0              # Solution counter

def promising(i: int) -> bool:
    global W, vcolor
    # Complete the code here
    j = 1
    while j < i:
        if W[i][j] == 1 and vcolor[i] == vcolor[j]:
            return False
        j += 1
    

    return True

def mcoloring(i: int, m: int) -> None: # (0, m)
    global n, vcolor, count
    if promising(i): # i는 현재 색칠된 정점의 수 (0으로 넘어옴)
        if i == n:
            print(vcolor[1:])
            # Complete the code here
            count += 1 
        else:
            # Complete the code here
            for j in range(1, m + 1):
                vcolor[i + 1] = j
                mcoloring(i + 1, m)
    return

            
