print('~' * 20)
print(f'{"Tabuada":^20}')
print('~' * 20)
print(' ')

p = cont = 0
n = int(input('Digite um número: '))
print('-=' * 20)
while cont <= 10:
    p = n * cont

    print(f'{n} x {cont} = {p}')
    cont += 1
    if cont > 10:
        print('-=' * 20)
        op = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
        if op in 'Ss':
            cont = 0
            n = int(input('Digite um numero: '))
        else:
            break
print('Fim.')
