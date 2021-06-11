n = 0
quant = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero: [999 para parar] '))
    if n != 999:
        soma += n
        quant += 1
print(f'Você digitou {quant} numeros\nE a soma de todos eles foi: {soma}')