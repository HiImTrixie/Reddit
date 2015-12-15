def generator():
    yield 2
    i = 3
    while True:
        yield i
        i += 2


#  distinct prime factors
def get_prime_factors(n):
    gen = generator()
    factors = set()
    i = gen.next()
    while n > 1:
        if n % i == 0:
            factors.add(i)
            n //= i
        else:
            i = gen.next()

    return factors


def pairs(*args):
    for arg in args:
        if sum(get_prime_factors(arg[0])) == sum(get_prime_factors(arg[1])):
            print arg, "VALID"
        else:
            print arg, "NOT VALID"

pairs((5, 6), (2107, 2108), (492, 493), (128, 129))
