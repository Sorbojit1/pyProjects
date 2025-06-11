import math
def fact_of_fact(value):
    result = 1
    for n in range(value,0,-1):
        fact = math.factorial(n)
        result *= fact
    return result
try:
    userInput = int(input('Enter an integer number \n- '))
    print(fact_of_fact(userInput))
except ValueError:
    print('Integer is only allowed or the factorial is too huge.')