print('Calculadora de radar 1.0')
v = float(input('Qual a velocidade do carro: Km/h '))
m = float((v - 80) * 7)
if v <= 80.0:
    print('A velocidade está dentro dos limites.')
else:
    print(f'A velocidade ultrapassa o limite de 80Km/h\nA multa é de: {m} R$ ')
