def Rabbit_Generation(n, k):
    if n < 2:
        return n
    else:
        return Rabbit_Generation(n-1, k) + Rabbit_Generation(n-2, k)*k

# print(Rabbit_Generation(35, 4)) -> 48127306357829

"""
principle -> 
    f1, f2 = f1 + k*f2, f1
        or
    fn = f1 + k*f2
    f2 = f1
    f1 = fn
"""

"""
sol #1
def fib(n, k):
    previous1, previous2 = 1, 1
    for i in range(2, n):
        previous1, previous2 = previous2, previous1 * k + previous2
    return previous2
    
sol #2
def fib(n,k=1):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1, k) + k * fib(n-2, k)
    
sol #3
memo = {}
def fib(n,k=1):
    args = (n, k)
    if args in memo:
        return memo[args]  # Aha! We have computed this before!

    # We haven't computed this before, so we do it now
    if n == 1:
        ans = 1
    elif n == 2:
        ans = 1
    else:
        ans = fib(n-1, k) + k * fib(n-2, k)
    memo[args] = ans  # don't forget to remember the result!
    return ans
"""