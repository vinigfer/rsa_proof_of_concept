from math import gcd
from random import randint
from sys import getrecursionlimit, setrecursionlimit


def find_prime_with_fermat(number_of_bits=1000):
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
        raise Exception('Sem inversão modular')

    return x % m


class RSA(object):
    @property
    def public_key(self):
        return self.n, self.e

    @property
    def private_key(self):
        return self.p, self.q, self.d

    def trabalho(self):
        # Need to increase max recursion for python stack
        # print(getrecursionlimit())
        setrecursionlimit(2000)

        self.create_prime_numbers()
        self.calculate_n()
        self.calculate_phi()
        self.generate_e()
        self.calculate_d()

    def create_prime_numbers(self):
        self.p = find_prime_with_fermat()
        self.q = find_prime_with_fermat()
        while self.p == self.q:
            self.q = find_prime_with_fermat()

    def calculate_n(self):
        self.n = self.p * self.q

    def calculate_phi(self):
        self.phi = (self.p - 1) * (self.q - 1)

    def generate_e(self):
        self.e = randint(1, self.phi)

        if self.e < 2 or gcd(self.e, self.phi) != 1:
            self.gerar_e()

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
