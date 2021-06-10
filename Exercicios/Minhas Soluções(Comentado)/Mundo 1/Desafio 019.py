# outro pacote, esse como o nome sugere, faz coisas aleatorias(ou pseudo-aleatorias... bla bla bla)
import random

print('sorteio de alunos')
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
r = [a1, a2, a3, a4]
# Listas ficam em colchetes
# o choice() vai sortear em uma lista, tupla, etc. Um resultado 
print('o aluno escolhido foi:', random.choice(r))


