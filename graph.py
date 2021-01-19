def logistic_map(r, l):
    return [r*i*(1-i) for i in l]

def logistic_iter(r, l, d):
    for i in range(d):
        l = logistic_map(r, l)
    return l
