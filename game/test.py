import random
import time
list = []
rand = 0

def rndm(any):
    rand = random.randint(0,30)
    if rand in list:
        rand = random.randint(0,30)
        rndm(0)
    else:
        list.append(rand)

while True:
    time.sleep(1)
    rndm(0)
    print(list)