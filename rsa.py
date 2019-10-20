from random import randint


def find_prime_with_fermat(number_of_bits=1024):
    MINIMUM = pow(2, number_of_bits)
    MAXIMUM = pow(2, number_of_bits + 1) - 1

    while True:
        p = randint(MINIMUM, MAXIMUM)
        if pow(2, p -1, p) == 1:
            print("Found prime number")
            return p
