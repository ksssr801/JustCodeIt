import time

# Finonacci series: 1,1,2,3,5,8,13,21,34,...
# Time: 2^n

# Fibonacci series with memoization to improve performance
fib_series = [1, 1]
def fib(n, memo={1: 1, 2: 1}):
    if n in memo.keys(): return (memo[n], fib_series)
    if n <= 2: return (1, fib_series)
    memo[n] = fib(n-1, memo)[0]+fib(n-2, memo)[0]
    fib_series.append(memo[n])
    return (memo[n], fib_series)

print ('for 10: ', fib(10))

