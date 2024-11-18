# itertools.product()
from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for vals in list(product(a, b)):
    print(vals, end=' ')
