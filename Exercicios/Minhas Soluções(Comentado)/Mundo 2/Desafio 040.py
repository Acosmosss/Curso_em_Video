n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(m)
if m == 7:
    print('Aprovado2')
elif 7 > m >= 5:
    print('recuperação')
elif m < 5:
    print('reprovado')
