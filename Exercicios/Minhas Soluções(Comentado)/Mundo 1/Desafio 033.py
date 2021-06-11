# dá pra fazer isso bem mais facilmente, mas o objetivo da aula era "ifs"  :/. 
n1 = int(input('Digite o Primeiro Número: '))
n2 = int(input('Digite o Segundo Número: '))
n3 = int(input('Digite o Terçeiro Número: '))
# verificando maior 
if n1 >= n2 and n1 >= n3:
    big = n1
if n2 >= n3 and n2 >= n1:
    big = n2
if n3 >= n2 and n3 >= n1:
    big = n3
# verificando menor
if n1 <= n2 and n1 <= n3:
    peq = n1
if n2 <= n1 and n2 <= n3:
    peq = n2
if n3 <= n1 and n2 <= n2:
    peq = n3
print(f'o maior numero é {big}')
print(f'O menor número é {peq}')
