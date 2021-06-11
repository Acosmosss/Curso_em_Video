r1 = float(input('Primeira Reta: '))
r2 = float(input('Segunda Reta: '))
r3 = float(input('Terceira Reta: '))
# de novo if "composto", por que triangulos só conseguem ser formados, se nenhuma das somas
# de duas retas for maior que a terceira.
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas PODEM formar um triângulo')
else:
    print('As retas NÃO PODEM formar um Triângulo')
