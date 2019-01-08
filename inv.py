from euclid import ex_euclid

def inv(a, n):
    result = ex_euclid(a, n)[0:2]
    d = result[0] % n
    x = result[1] % n
    if d == 1:
        return x
    else:
        None
