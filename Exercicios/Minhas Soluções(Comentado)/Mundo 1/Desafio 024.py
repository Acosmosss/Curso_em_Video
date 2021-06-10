print('Detector de santo')
cep = str(input('Digite o nome da sua cidade: ')).strip()
analise = cep.lower().find('santo')
# Eu fiz uma gambiarra aqui, usando o replace, para substituir o 0 da find(que responde com -1 ou 0)
# e substituindo pela string lá embaixo. 
print(str(analise).replace('0', 'sua cidade contem santo, amém')) # Santo berço devora! 
