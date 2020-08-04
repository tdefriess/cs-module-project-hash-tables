# Your code here
import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y, table):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    v = math.pow(x, y)
    v = table[v]
    v //= (x + y)
    v %= 982451653
    return v
    
def factorial(n, cache={}):
    if n == 2:
        return 2
    else:
        cache[n] = n * factorial(n, cache)

    return cache

fact_table = factorial(14 ** 6)


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y, fact_table)}')
