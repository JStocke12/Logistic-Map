from PIL import Image

res = 10

img = Image.new('RGB', (res*3, res))

px = img.load()

def logistic_map(r, l):
    return [r*i*(1-i) for i in l]

def logistic_iter(r, l, d):
    for i in range(d):
        l = logistic_map(r, l)
    return l

for r in [i/res for i in range(res, res*4)]:
    print([j//(1/res) for j in logistic_iter(r, [1-(i/10) for i in range(10)], 20)])

img.save('image.png')
