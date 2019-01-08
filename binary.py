from inv import inv

# return y = g^k mod n
def mod_binary(k, g, n):
    if k == 0:
        return 1

    k = [int(s) for s in format(k, 'b')]
    y = g
    for i in k[1:]:
        if i == 1:
            y = (y**2%n)*g % n
        else:
            y = y**2 % n

    return y

def crt(mod_list, value_list):
    if len(mod_list) != len(value_list):
        return None

    n = mod_list[0]
    m = value_list[0]
    for i in range(len(mod_list))[1:]:
        x = inv(mod_list[i], n)
        if x == None:
            return None
        n *= mod_list[i]
        m = (value_list[i]+mod_list[i]*x*(m-value_list[i])) % n

    return m

def mod_crt_binary(value_list, g, mod_list):
    value_list4CRT = []
    for i in range(len(mod_list)):
        value_list4CRT.append(mod_binary(value_list[i], g, mod_list[i]))
    x = crt(mod_list, value_list4CRT)
    return x
