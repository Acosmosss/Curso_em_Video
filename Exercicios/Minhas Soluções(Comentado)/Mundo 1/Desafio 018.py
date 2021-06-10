from math import tan, cos, sin, radians
#simplificando imports, para simplificar, na hora de "chamar" os comandos 
print('calculadora de tangente para preguiçosos') # eu de novo :) 
ang = float(input('Digite um ângulo: ')) 
# se não tivesse feito daquela maneira, teria que usar math.tan(), math.cos(), etc.
tan = tan(radians(ang))
cos = cos(radians(ang))
sin = sin(radians(ang))
print(f'Seu Ângulo {ang}° possui\nseno: {sin:.2f} \nCosseno: {cos:.2f} \nTangente: {tan:.2f}')
