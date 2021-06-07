from math import tan, cos, sin, radians
print('calculadora de tangente para preguiçosos')
ang = float(input('Digite um ângulo: '))
tan = tan(radians(ang))
cos = cos(radians(ang))
sin = sin(radians(ang))
print(f'Seu Ângulo {ang}° possui\nseno: {sin:.2f} \nCosseno: {cos:.2f} \nTangente: {tan:.2f}')
