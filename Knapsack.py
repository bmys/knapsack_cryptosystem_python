from random import randint


# generate private key
def super_increasing(n1, count):
    total_sum = n1
    yield n1
    for i in range(count):
        new_value = total_sum + randint(1, 25)
        total_sum += new_value
        yield new_value


def create_public_key(private, n, m):
    suma = sum(private)
    if suma >= m:
        raise AttributeError('m value should be greater than sum of private key')
    return [(k * n) % m for k in private]


def encode(sequence, s_number):
    output = list()
    for i in reversed(sequence):
        if s_number >= i:
            output.append(1)
            s_number -= i
        else:
            output.append(0)
    if s_number == 0:
        return list(reversed(output))
    else:
        raise AttributeError("No solutions for this attributes")


def to_cipher(plain, seq):
    return sum([i * j for i, j in zip(plain, seq)])


def to_plain(cipher, n, m):
    return cipher * n % m


def inverse_mod(n, m):
    i = 1
    while True:
        val = (n * i) % m
        if val == 1:
            return i
        else:
            i += 1
