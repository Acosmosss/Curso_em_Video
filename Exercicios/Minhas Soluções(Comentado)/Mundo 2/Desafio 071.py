print('Banco')
valor = int(input('Quanto você quer sacar?'))
ced = 50
totced = 0
total = valor
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'{totced} de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
