import math
print('calculador de hipotenusa para preguiçosos')
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('digite o comprimento do cateto adjacente: '))
hipo = math.hypot(co, ca)
print(f'Seu triadngulo de catetos {co}, {ca} \ntem a hipotenusa com comprimento de {hipo}')
