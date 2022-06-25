import math
import random
import time

import number_generator
import progressbar

# import matplotlib.pyplot as plt

import csv

# generate a prime number with a given bit size
def generate_prime(number_size):
    x = True
    y = 0
    while x:
        y = random.getrandbits(number_size)
        x = not is_prime(y)
    return y


# check if the given number is a prime
def is_prime(number):
    for index in range(2, int(math.sqrt(number)) + 1):

        if (number % index) == 0:
            return False
    return True

#
#
#
#
#

def modular_pow(base, exponent, modulus):
    # initialize result
    result = 1

    while (exponent > 0):

        # if y is odd, multiply base with result
        if (exponent & 1):
            result = (result * base) % modulus

        # exponent = exponent/2
        exponent = exponent >> 1

        # base = base * base
        base = (base * base) % modulus

    return result


# method to return prime divisor for n
def PollardRho(n):
    # no prime divisor for 1
    if (n == 1):
        return n

    # even number means one of the divisors is 2
    if (n % 2 == 0):
        return 2

    # we will pick from the range [2, N)
    x = (random.randint(0, 2) % (n - 2))
    y = x

    # the constant in f(x).
    # Algorithm can be re-run with a different c
    # if it throws failure for a composite.
    c = (random.randint(0, 1) % (n - 1))

    # Initialize candidate divisor (or result)
    d = 1

    # until the prime factor isn't obtained.
    # If n is prime, return n
    while (d == 1):

        # Tortoise Move: x(i+1) = f(x(i))
        x = (modular_pow(x, 2, n) + c + n) % n

        # Hare Move: y(i+1) = f(f(y(i)))
        y = (modular_pow(y, 2, n) + c + n) % n
        y = (modular_pow(y, 2, n) + c + n) % n

        # check gcd of |x-y| and n
        d = math.gcd(abs(x - y), n)

        # retry if the algorithm fails to find prime factor
        # with chosen x and c
        if (d == n):
            return PollardRho(n)

    return d


#
#
#
#
#

def rsa_factoring(total_iterations):
    base_size = 30
    divisor = 0

    for i in range(total_iterations):
        divisor_equal = False
        file = open("data_analysis/results.csv", "a")
        p = generate_prime(base_size)
        q = generate_prime(base_size)
        n = p * q

        print(f"checking {n}")
        start_time = time.time()
        try:
            divisor = PollardRho(n)
        except RecursionError:
            print("maximum recursion depth")
        end_time = time.time() - start_time

        if(divisor == p) | (divisor == q):
            divisor_equal = True
            print("divisor equals the prime number")

        print("checking n=", n, "took", round(end_time, 4), "s", "divisor =", divisor)
        progressbar.progress(i, total_iterations)
        file.write(f"{n};{p};{q};{divisor};{end_time};{divisor_equal};{base_size}\n")
        file.close()

        base_size = random.randint(35, 40)

    return

#
#
#
#
#


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')

    loops = 20
    selection = 1

    if selection == 1:
        rsa_factoring(loops)
    if selection == 2:
        number_generator.number_generator(loops)







