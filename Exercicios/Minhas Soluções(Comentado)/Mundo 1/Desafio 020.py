from random import shuffle

print('sorteio de lista de aluno')
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
r = [a1, a2, a3, a4]
# o shuffle, vai embaralhar a lista. Perceba que eu criei outra variavel para armazenar a lista embaralhada,
# enquanto a original permanece intacta, por isso daria pra usar o shuffle em tuplas.
rand = shuffle(r)
print(r)
