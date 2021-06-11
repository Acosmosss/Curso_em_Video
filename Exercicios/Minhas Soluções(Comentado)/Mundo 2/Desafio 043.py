h = float(input('Sua Altura: m '))
w = float(input('Seu peso: kg '))
imc = w / (h ** 2)
print(f'Seu IMC está em: {imc:.1f} kg/m²')
if imc <= 18.5:
    cla = 'Magreza!'
elif imc <= 25:
    cla = 'Peso Ideal!'
elif imc <= 30:
    cla = 'Sobrepeso!'
elif imc <= 40:
    cla = 'Obesidade!'
elif imc > 40:
    cla = 'Obesidade Mordbida!'


print(f' CLASSIFICÃO: {cla}')
