s = 0  # Acumulador
c = 0  # Contador
for n in range(1, 501, 2):
    if n % 3 == 0:
        c += 1
        s += n
print(f' a soma de todos os {c} numeros impares e multiplos de 3, de 1 á 500 é igual á {s}')
