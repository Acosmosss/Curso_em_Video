print('progressão aritmética')
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print(pt, end=' - ')
termos = 1
while termos != 10:
    pt += r
    print(pt, end=' - ')
    termos += 1
print('Fim.')
