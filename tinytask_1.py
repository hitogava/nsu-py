import math

def twoComplement(x):
    p = 2**(math.floor(math.log(x,2)) + 2) - 1
    return p-x+1
    

def getBitsCount(x):
    t = x
    count=0
    while t > 0:
        count += t%2
        t//=2
    return count

x = int(input())
if x < 0:
    x = twoComplement(abs(x))
print(getBitsCount(x))
