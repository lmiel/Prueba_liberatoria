m = 1000000

"""def fibonacci(n):
    a = 0 
    b == 1
    for i in range(n):
        a = b
        b = a + b
    return b"""

def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b
  
print(fibonacci(9))
