print('Detector de santo')
cep = str(input('Digite o nome da sua cidade: ')).strip()
anal = cep.lower().find('santo')
print(str(anal).replace('0', 'sua cidade contem santo, amém'))
