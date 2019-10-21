from math import gcd
from random import randint
from time import sleep
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
    def chave_publica(self):
        return self.n, self.e

    @property
    def chave_privada(self):
        return self.p, self.q, self.d

    def trabalho(self):
        # Need to increase max recursion for python stack
        # print(getrecursionlimit())
        setrecursionlimit(2000)
        self.gerar_primos()
        self.calcular_n()
        self.calcular_phi()
        self.gerar_e()
        self.calcular_d()

    def gerar_primos(self):
        self.p = find_prime_with_fermat()
        self.q = find_prime_with_fermat()
        while self.p == self.q:
            self.q = find_prime_with_fermat()

    def calcular_n(self):
        self.n = self.p * self.q

    def calcular_phi(self):
        self.phi = (self.p - 1) * (self.q - 1)

    def gerar_e(self):
        self.e = randint(1, self.phi)

        if self.e < 2 or gcd(self.e, self.phi) != 1:
            self.gerar_e()

    def calcular_d(self):
        self.d = modinv(self.e, self.phi)

    # def gerar_chaves(self, bits=64):
    #     self.gerar_primos(int(bits / 2))
    #     self.calcular_n()
    #     self.calcular_phi()
    #     self.gerar_e()
    #     self.calcular_d()

    @staticmethod
    def encriptar(mensagem, chave_publica):
        n, e = chave_publica

        mensagem_ascii = [ord(caractere) for caractere in mensagem]
        mensagem_encriptada = [str(pow(caractere_ascii, e, n)) for caractere_ascii in mensagem_ascii]

        return ' '.join(mensagem_encriptada)

    @staticmethod
    def desencriptar(mensagem_encriptada, chave_privada=None):
        p, q, d = chave_privada

        mensagem_encriptada = mensagem_encriptada.split(' ')
        mensagem_ascii = [pow(int(caractere_encriptado), d, p * q) for caractere_encriptado in mensagem_encriptada]
        mensagem = [chr(caractere_ascii) for caractere_ascii in mensagem_ascii]

        return ''.join(mensagem)
