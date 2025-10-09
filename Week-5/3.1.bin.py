import time

def bin(n: int, k: int) -> int:
    if k == 0 or n == k:
        return 1
    else:
        # Complete the code here
        # 파스칼의 삼각형 - 이항 계수 구하기
        return bin(n-1, k-1) + bin(n-1, k)


