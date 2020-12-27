import math

def decryption(encryption, j, n):
    power = encryption ** j
    newNum = math.floor(power / n) * n
    return (power - newNum)
