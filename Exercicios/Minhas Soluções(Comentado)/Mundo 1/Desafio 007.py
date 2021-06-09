#tem muita coisa para explicar nesse :T

print('Sistema de notas do Colegio Nostradamus') # Agatha :,(
# import, importa pacotes que não são "nativos" do python, nesse caso o pacote time, serviu para para fazer
# o programa esperar(sleep) para mostrar o resultado.
import time
# chamando a função sleep do pacote time, e fazendo o programa esperar 1 segundo. 
# é bem desnecessário aqui mas eu tava experimentando :P   
time.sleep(1)
nome = input('Insira o nome do aluno: ')
nota1 = float(input('primeira nota do aluno: '))
nota2 = float(input('segunda nota do aluno: '))
media = (nota1 + nota2) / 2
# As f strings, servem como o .format, só que a variável é colocada dentro das chaves (bem mais simples :I)
# como notas só tem um numero dps do ponto décimal, a formatação ":.1f" mostra somente um número após o ponto   
# o "\n" serve para quebrar a linha. 
print(f'Aluno:{nome:=^20}\nPrimeira unidade:{nota1:.1f}\nSegunda unidade: {nota2:.1f}\nMédia: {media:.1f}')

# introdução dos Ifs :P 
#basicamente Se(if) a media for maior que(>) 6.0, ele vai executar o que está na indentação. 
if media > 6.0: # não esquece dos dois pontos 
    print('PASSED!'.center(40, '='))
# senão (else) ele vai executar o que está nessa indentação. 
else:
    print('FAILED!'.center(40, '='))
