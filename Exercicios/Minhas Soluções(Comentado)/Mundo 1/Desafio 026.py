print('Detector de AAAAAAAAAAAAAAAAAA')
frase = str(input('Digite uma frase: ').strip().upper())
cont = frase.count('A')
pri = int(frase.find('A')) + 1
ult = frase.rfind('A') + 1
print(f'A frase: {frase}\ncontem {cont} letras A\nA primeira letra A aparece na posição {pri}\nA ultima letra A aparece'
      f' na posição {ult}')
