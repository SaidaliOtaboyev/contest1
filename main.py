#saidali
import random
from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import decorator_1

@decorator_1
def func():
    print("I am ready to Start")
    gonetime = 0
    n = random.randint(10, 751)
    for i in range(n):
         gonetime += (i ** 2)
    return  gonetime 

@decorator_1
def funx(n=None):
    print("I am ready to do serious stuff")
    uzbeksila = float('-inf')

    if n is None:
        n = random.randint(10, 751)

    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > uzbeksila:
            uzbeksila = i
    return uzbeksila 

if __name__ == "__main__":
    func()
    funx()
    func()
    funx()
    func()
