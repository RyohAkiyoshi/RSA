from binary import mod_binary

def encrypt(m, n, e):
    return mod_binary(e, m, n)
