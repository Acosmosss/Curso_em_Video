sal = float(input('Digite o salário do funcionario: R$ '))
aum = 15
if sal >= 1250.00:
    aum = 10
ca = sal * aum / 100
novo = sal + ca
print(f'O salário sofreu um aumento de {ca:.2f} R$\nO novo salário é: {novo:.2f} R$  ')
