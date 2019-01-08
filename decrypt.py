from binary import mod_crt_binary

def decrypt(c, dp, dq, p, q, qinv):
    return mod_crt_binary([dp, dq], c, [p, q])
