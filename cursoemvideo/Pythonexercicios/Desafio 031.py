viagem = float(input('Digite a distancia da viagem: Km '))
if viagem > 200:
    preco = viagem * 0.45
    print(f'Sua viagem vai custar: {preco} R$')
else:
    preco = viagem * 0.50
print(f'Sua viagem vai custar: {preco} R$')
