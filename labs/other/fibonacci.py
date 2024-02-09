 
def fibonacci_of(n: int) -> int:
    if n in [0, 1]:
        return n    
    return fibonacci_of(n-1) + fibonacci_of(n-2)



def tribonacci(n: int) -> int:
    if n in [0, 1]:
        return n    
    elif n == 2:
        return 1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


for i in range(10):
    print(tribonacci(i))