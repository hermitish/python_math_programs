# primes_in_range.py
# takes an upper and lower limit and returns list of all primes in the range

def prime_check(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 1/2) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(l, u):
    lst = []
    for i in range(l, u + 1):
        if prime_check(i):
            lst.append(i)
    return lst
l = int(input("Enter lower limit: "))
u = int(input("Enter upper limit: "))
for x in primes_in_range(l, u):
    print(x, end=' ')
