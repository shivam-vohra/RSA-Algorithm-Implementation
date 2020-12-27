import random
import math

def getPVal(primes):
    return random.choice(primes)

def getQVal(primes):
    return random.choice(primes)

def getN(p, q):
    return p * q

def getZ(p, q):
    return (p - 1) * (q - 1)

def isCoPrime(z):
    coPrimes = []
    for i in range(1, z):
        if z % i != 0:
            coPrimes.append(i)
    return random.choice(coPrimes)

def getKVal(z):
    return isCoPrime(z)

def findSecretKey(k, z):
    possibilities = []
    for i in range(1, z * 2):
        if k * i % z == 1:
            possibilities.append(i)
    return random.choice(possibilities)

print(findSecretKey(7108, 13600))