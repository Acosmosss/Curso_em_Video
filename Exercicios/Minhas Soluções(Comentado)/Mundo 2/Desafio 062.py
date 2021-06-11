print('Progressão aritmética')
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
t = int(input('Quantos termos você mostrar: '))
print(pt, end=" - ")
parar = 1
while parar != t:
    pt += r
    print(pt, end=" - ")
    parar += 1
print('Fim.')

