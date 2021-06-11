print('calculadora primitiva')
r = 0
sair = 0
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
while sair == 0:

    op = int(input('''O que você quer fazer com esses numeros:
    [1] Somar
    [2] multiplicar
    [3] Qual maior? 
    [4] Outros valores
    [5] Sair
     Qual sua escolha: '''))
    if op == 1:
        print(f'A soma dos numeros {n1} + {n2} = {n1 + n2}')
    elif op == 2:
        print(f'O produto da multiplicação {n1} x {n2} = {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é o maior número.')
        else:
            print(f'{n2} é o maior número')
    elif op == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif op == 5:
        print('Até a proxima!')
        sair += 1
