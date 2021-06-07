from random import shuffle

print('sorteio de lista de aluno')
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
r = [a1, a2, a3, a4]
rand = shuffle(r)
print(r)
