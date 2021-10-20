from decimal import Decimal
from math import factorial
import decimal

def pi(n):
    X = Decimal(0)
    k = 0
    while k < n:
        X += ((Decimal(-1)**k) * (Decimal(factorial(6 * k))) * (13591409 + 545140134 * k))/((factorial(k)**3) * (factorial(3 * k)) * (640320**(3 * k))*Decimal(640320**3).sqrt())
        k += 1
    X = 12*X
    X = X**(-1)
    return X

n = int(input())
decimal.getcontext().prec = n+1
print (pi(n))
