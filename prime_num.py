def genPrimes():
    prime = 1
    primes = []
    while True:
        prime += 1
        isprime = True
        for p in primes:
            if prime % p == 0:
                isprime = False
        if isprime:
            primes += [prime]
            yield prime



c = genPrimes()
