print('$ Bem vindo a central salarial da Rope.Inc $')
func = input('Qual funcionario receberá aumento: ')
aumpor = float(input('Porcetagem de aumento: %'))
SA = float(input(f'Qual salario atual do Funcionario {func}: R$'))
aum = SA + (SA * aumpor /100)
print(f'O funcionario {func}, receberá o aumento de {aumpor:.2f} R$, e passará a receber {aum:.2f} R$ agora'
      f' \nsalario anterior: {SA:.2f} R$ ')