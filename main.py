#saidali
import random
from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import decorator_1

@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)
    return result 

@decorator_1
def funx(n=None):
    print("I am ready to do serious stuff")
    max_val = float('-inf')

    if n is None:
        n = random.randint(10, 751)

    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i
    return max_val 

if __name__ == "__main__":
    func()
    funx()
    func()
    funx()
    func()
