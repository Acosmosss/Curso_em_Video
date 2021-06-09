import time

print('Programa de conversão de Metros')
m = float(input('insira a metragem: '))
# outro sleep desnecessario :P 
time.sleep(1)
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print(f'Conversão de {m}m\nquilômetros: {km:.5f}km\nHectômetros: {hm:.4f}hm\nDecâmetros: {dam:.4f}dam\nDecímetros: {dm}dm\nCentímetros: {cm:.0f}cm'
      f'\nMilímetro: {mm:.0f}mm')