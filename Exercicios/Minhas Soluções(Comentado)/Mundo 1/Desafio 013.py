print('$ Bem vindo a central salarial da Rope.Inc $') # as primeiras 2 linhas são inuteis mas eu gosto de 
func = input('Qual funcionario receberá aumento: ')   # inventar historias para cada codigo kkkk :)
aumporcento = float(input('Porcetagem de aumento: %'))
SA = float(input(f'Qual salario atual do Funcionario {func}: R$'))
# lembrando a ordem de operações, a operação em parentesis vai acontecer primeiro do que a soma fora
# (já aconteceria isso do mesmo jeito, multiplicações e divisões acontecem primeiro do que somas. ) 
aumento = SA + (SA * aumporcento /100)
print(f'O funcionario {func}, receberá o aumento de {aumporcento:.2f} R$,'
f' e passará a receber {aumento:.2f} R$ agora'
      f' \nsalario anterior: {SA:.2f} R$ ')