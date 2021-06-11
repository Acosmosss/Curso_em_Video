print('calculadora de fatorial')
n1 = int(input('Digite o numero: '))
r = n1
print(f'Calculando {n1}! = {n1} x', end=' ')
while r > 1:
    r -= 1
    print(r, end=' ')
    print(' x ' if r > 1 else ' = ', end=' ')
    n1 *= r
print(n1)
