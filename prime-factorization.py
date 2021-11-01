import time

def check_is_prime(n):
    # multiples = list(m for m in range(1, n) if n%m == 0)
    multiples = list(m for m in range(1, int(n/2)) if n%m == 0)
    return multiples, len(multiples) == 1

def find_prime_factors(multiples: list):
    i = 1
    prime_factors = list(pf for pf in multiples if check_is_prime(pf)[1])
    return prime_factors

def process(n: int):
    start = time.time()
    mx = check_is_prime(n)
    end = time.time()
    print('The time for finding prime or not', end-start)
    if(mx[1]):
        print(n, 'is a prime number')
    else:
        print(n, 'is a composite number')
        print('prime factors:', find_prime_factors(mx[0]))

process(31)
process(2179433)