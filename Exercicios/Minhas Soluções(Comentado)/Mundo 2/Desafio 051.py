pt = int(input('Digite o primeiro Termo: '))
r = int(input('Digite a razão: '))
d = pt + (10 - 1) * r
for pa in range(pt, d + r, r):
    print(pa, end=' - ')
print(f'Acabou')
