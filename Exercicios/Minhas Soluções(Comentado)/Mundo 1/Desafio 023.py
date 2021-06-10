# Esse aqui pega cada numero de um número, e divide ele nas unidades, de unidade, dezena, centena, milhar.
n1 = int(input('Digite um número: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print(f'\nMilhar: {m}\nCentena: {c}\nDezena: {d}\nUnidade: {u}')
