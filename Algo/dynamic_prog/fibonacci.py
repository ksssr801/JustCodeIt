# Finonacci series: 1,1,2,3,5,8,13,21,34,...
# Time: 2^n

def fib(n):
    if n <= 2: return 1
    return fib(n-1)+fib(n-2)

try: 
    num = int(input())
    # this is pretty slow for larger value of num
    print (fib(num))
except: print ("Only positive number is allowed.")
