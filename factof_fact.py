import math
def fact_of_fact(value:int):
    result = 1
    for n in range(value,0,-1):
        fact = math.factorial(n)
        result *= fact
    return result

print(fact_of_fact(2))