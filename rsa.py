"""
Implementacao do algoritmo RSA em python3.7
Autor: Vinicius Ferreira
Data: 24/Outubro/2019
Como usar: consulte o arquivo README.md
"""

from math import gcd
from random import randint
from sys import getrecursionlimit, setrecursionlimit


def find_prime_with_fermat(number_of_bits=1024):
    MINIMUM = pow(2, number_of_bits)
    MAXIMUM = pow(2, number_of_bits + 1) - 1
    while True:
        p = randint(MINIMUM, MAXIMUM)
        if pow(2, p -1, p) == 1:
            return p


def egcd(a_value, b_value):
    if a_value == 0:
        return b_value, 0, 1
    g, x, y = egcd(b_value % a_value, a_value)
    return g, y - (b_value // a_value) * x, x


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("No modular inversion")
    return x % m


class RSA(object):
    def __init__(self):
        # Often we hit the maximum recursion stack for python (which is 1000) during egcd method.
        # Here we stretch the limit a bit further, as from tests we only needed a few more iterations.
        # print(getrecursionlimit())
        setrecursionlimit(2000)

    @property
    def public_key(self):
        return self.n, self.e

    @property
    def private_key(self):
        return self.p, self.q, self.d

    def setup(self):
        """Run in a single batch all the necessary requirements to get RSA encryption working"""

        # We can also call methods set_p and set_q manually if we already have the prime_numbers
        self.create_prime_numbers()

        self.calculate_n()
        self.calculate_phi()
        self.generate_e()
        self.calculate_d()

    def create_prime_numbers(self):
        self.set_p(find_prime_with_fermat())
        self.set_q(find_prime_with_fermat())
        while self.p == self.q:
            self.set_q(find_prime_with_fermat())

    def set_p(self, p):
        self.p = p

    def set_q(self, q):
        self.q = q

    def calculate_n(self):
        self.n = self.p * self.q

    def calculate_phi(self):
        self.phi = (self.p - 1) * (self.q - 1)

    def generate_e(self):
        self.e = randint(1, self.phi)
        if self.e < 2 or gcd(self.e, self.phi) != 1:
            self.generate_e()

    def calculate_d(self):
        self.d = modinv(self.e, self.phi)

    @staticmethod
    def encrypt(message, public_key):
        n, e = public_key
        ascii_message= [ord(letter) for letter in message]
        encrypted_message = [str(pow(ascii_letter, e, n)) for ascii_letter in ascii_message]
        return ' '.join(encrypted_message)

    @staticmethod
    def decrypt(encrypted_message, private_key):
        p, q, d = private_key
        encrypted_message = encrypted_message.split(' ')
        ascii_message = [pow(int(encrypted_letter), d, p * q) for encrypted_letter in encrypted_message]
        message = [chr(ascii_letter) for ascii_letter in ascii_message]
        return ''.join(message)
