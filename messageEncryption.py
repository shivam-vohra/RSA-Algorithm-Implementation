import math

def findEncryption(plainMessage, k, n):
    power = plainMessage ** k
    newNum = math.floor(power / n) * n
    return (power - newNum)


