totmaior = 0
totmenor = 0
print('Maior e Menor peso')
for pessoa in range(1, 6):
    peso = float(input(f'Digite o peso da {pessoa}° pessoa: '))
    if pessoa == 1:
        totmaior = peso
        totmenor = peso
    else:
        if peso > totmaior:
            totmaior = peso
        if peso < totmenor:
            totmenor = peso
print(f'O maior peso da lista foi {totmaior}.\nE o menor foi {totmenor}.')
