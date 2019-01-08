from fermat import fermat_prime_gen
from lcm import lcm
from euclid import euclid
from inv import inv
from random import randint
from is_prime import is_prime

# Input: Bit length of n
# Output: n, e, d, dp, dq, qinv
# (dp = d mod (p-1), dq = d mod (q-1), qinv = q^(-1) mod p)
def rsa_keygen(keysize):
    if keysize < 5:
        return None

    # p
    psize = int(keysize / 2)
    p = fermat_prime_gen(randint(2**(psize-1)-1, 2**psize-1), 1)
    if len(format(p, 'b')) > psize:
        p = fermat_prime_gen(2**(psize-1)-1, 1)
    while not is_prime(p):
        p = fermat_prime_gen(p, 1)

    # q
    qsize = keysize - psize
    q = fermat_prime_gen(randint(2**(qsize-1)-1, 2**qsize-1), 1)
    if len(format(q, 'b')) > qsize:
        q = fermat_prime_gen(2**(qsize-1)-1, 1)
    while not is_prime(q):
        q = fermat_prime_gen(q, 1)

    # n
    n = p * q

    # e
    l = (p-1) * (q-1)
    e = fermat_prime_gen(randint(2,l-1), 1)
    if e > l:
        e = fermat_prime_gen(l-1, 1)
    while not is_prime(e) and lcm(l, e) != 1:
        e = fermat_prime_gen(e, 1)

    d = inv(e, l)
    dp = d % (p-1)
    dq = d % (q-1)
    qinv = inv(q, p)
    return n, e, d, dp, dq, p, q, qinv
