def euclid(a0, b0):
    a = sorted([a0, b0], reverse = True)
    i = 1

    while a[i] != 0:
        a.append(a[i-1] % a[i])
        i += 1

    return a0


def ex_euclid(a0, b0):
    a = sorted([a0, b0], reverse = True)
    x = [1, 0]
    y = [0, 1]
    i = 1
    q = []

    while a[i] != 0:
        q.append(int(a[i-1]/a[i]))
        a.append(a[i-1]%a[i])
        x.append(x[i-1]-q[i-1]*x[i])
        y.append(y[i-1]-q[i-1]*y[i])
        i += 1

    d = a[i-1]
    if a0 > b0:
        return d, x[i-1], y[i-1]
    else:
        return d, y[i-1], x[i-1]
