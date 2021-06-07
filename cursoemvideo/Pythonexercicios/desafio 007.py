print('Sistema de notas do Colegio Nostra Damus')
import time
time.sleep(1)
nome = input('Insira o nome do aluno: ')
n1 = float(input('primeira nota do aluno: '))
n2 = float(input('segunda nota do aluno: '))
m = (n1 + n2) / 2
print(f'Aluno:{nome:=^20}\nPrimeira unidade:{n1:.1f}\nSegunda unidade: {n2:.1f}\nMédia: {m:.1f}')
if m > 6.0:
    print('PASSED!'.center(40, '='))
if m < 6.0:
    print('FAILED!'.center(40, '='))
