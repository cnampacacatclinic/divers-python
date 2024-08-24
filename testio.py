a = ['foo', 'bar', 'baz', 'qux', 'corge']

while a:
    if len(a) < 3:
        break
    print(a.pop())
print('Done.')

d = {'a': 0, 'b': 1, 'c': 0}

if d['a'] > 0:
    print('yeah !')
elif d['b'] > 0:
    print('yeah !')
elif d['c'] > 0:
    print('ok')
elif d['d'] > 0:
    print('ok')
else:
    print('not ok')

if 'bar' in {'foo': 1, 'bar': 2, 'baz': 3}:
    print(1)
    print(2)
    if 'a' in 'qux':
        print(3)
print(4)

import random

panier = ["Pomme", "Poire", "Banane", "Ananas", "Orange"]
resultat = panier[random.randint(0, 4)]
print(resultat)