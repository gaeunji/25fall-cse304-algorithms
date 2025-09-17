# name: 
# student id: 
def fib2(n: int) -> int:
    f = [0] * (n + 1)
    # Complete the code here
    # memoization 기법 사용
    
    f[0] = 0
    if n >= 1:
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]

    return f[n]