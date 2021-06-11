s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Informe o {c}º valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
if cont == 1:
    print(f'O unico número par foi: {s}')
else:
    print(f'A soma de {cont} números pares foi: {s}')
