r1 = int(input('primeira reta: '))
r2 = int(input('segunda reta: '))
r3 = int(input('terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo.')
else:
    print('As retas NÃO podem formar um triângulo')
    quit()
if r1 == r2 == r3:
    print('equilatero')
elif r1 == r2 or r2 == r3 or r1 == r3:
    print('isosceles')
else:
    print('escaleno')
