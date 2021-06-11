while True:
    print('=-' * 18)
    print(f'{"Detector de números primos":^35}')
    print('=-' * 18)
    n = int(input('Digite um número: '))
    tot = 0
    for p in range(1, n + 1):
        if n % p == 0:
            print('\033[33m', end=' ')
            tot += 1
        else:
            print('\033[31m', end=' ')
        print(f'{p}', end=' ')
    print(f'\n\033[mO número {n} foi dividido {tot} vezes ')
    if tot == 2:
        print('Por isso ele é um número primo.')
    else:
        print('Por isso ele não é um número primo.')
    op = input('Quer analizar outro número? (sim/não): ').strip().lower()
    if op == 'sim':
        print('\n' * 100)
    else:
        break
