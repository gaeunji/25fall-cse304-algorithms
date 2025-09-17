# name: 
# student id: 
def fib1(n: int) -> int:
    # Complete the code here
    
    #n번째 피보나치 수 구하기
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)
    
    