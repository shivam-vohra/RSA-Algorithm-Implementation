import math
import random
import primes
import keyGenerator
import messageDecryption
import messageEncryption

def rsaAlgo():
    primeNumbers = primes.getPrimes()
    p = keyGenerator.getPVal(primeNumbers)
    print(p)
    q = keyGenerator.getQVal(primeNumbers)
    print(q)
    n = keyGenerator.getN(p, q)
    print(n)
    z = keyGenerator.getZ(p, q)
    print(z)
    k = keyGenerator.getKVal(z)
    print(k)
    secretKey = keyGenerator.findSecretKey(k, z)

    plainMessage = int(input('What is the plain message text you want to encrypt as a label: '))

    encrypted_message = messageEncryption.findEncryption(plainMessage, k, n)

    decryptedMessage = messageDecryption.decryption(encrypted_message, secretKey, n)

    if (decryptedMessage == plainMessage):
        print('Encryption and decryption was a success!')
    else:
        print('Failed encryption and decryption.')


if __name__ == '__main__':
    rsaAlgo()