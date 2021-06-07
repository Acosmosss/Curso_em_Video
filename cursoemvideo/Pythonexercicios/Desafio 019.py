import random
print('sorteio de alunos')
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
r = [a1, a2, a3, a4]
# Listas ficam em colchetes
print('o aluno escolhido foi:', random.choice(r))


