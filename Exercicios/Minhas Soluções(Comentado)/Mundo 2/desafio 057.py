sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]:  ')).strip().upper()

    if sexo == 'M':
        print('bem vindo!')
    elif sexo == 'F':
        print('bem vinda!')
    else:
        print(f'{sexo} NÃO é uma resposta válida.')
