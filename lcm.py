from euclid import euclid

def lcm(a, b):
    return int(a * b / euclid(a,b))
