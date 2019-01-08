from binary import mod_binary

def fermat_judge(a, n):
    return mod_binary(n-1,a,n) == 1


def fermat_prime_gen(iv, n):
    p = iv + 1
    while True:
        for i in range(n):
            if not fermat_judge(p-(i+1), p):
                break
            if i == n-1:
                return p
        p += 1

