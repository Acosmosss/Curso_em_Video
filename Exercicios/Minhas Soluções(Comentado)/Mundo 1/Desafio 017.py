# Importando pacotes
import math
# o pacote math serve para realizar alguns calculos que o python sozinho não consegue
# Como por exemplo o .hypot() que calcula a hipotenusa de dois valores(ângulos)
print('calculador de hipotenusa para preguiçosos') # Sou eu 
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('digite o comprimento do cateto adjacente: '))
hipo = math.hypot(co, ca)
print(f'Seu triadngulo de catetos {co}, {ca} \ntem a hipotenusa com comprimento de {hipo}')
