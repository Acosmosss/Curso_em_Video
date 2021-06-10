print('Detector de AAAAAAAAAAAAAAAAAA')  # AAAAAAAAAAAAAAAAAAAAA
frase = str(input('Digite uma frase: ').strip().upper())
cont = frase.count('A')
pri = int(frase.find('A')) + 1
ult = frase.rfind('A') + 1
print(f'A frase: {frase}\n'
      f'contem {cont} letras A'
      f'\nA primeira letraA aparece na posição {pri}'
      f'\nA ultima letra A aparece'
      f' na posição {ult}')
