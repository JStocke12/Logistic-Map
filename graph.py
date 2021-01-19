def logistic_map(r, l):
    return [r*i*(1-i) for i in l]

def logistic_iter(r, l, d):
    for i in range(d):
        l = logistic_map(r, l)
    return l

print([1-(i/10) for i in range(10)], logistic_iter(3.2, [1-(i/10) for i in range(10)], 20))
