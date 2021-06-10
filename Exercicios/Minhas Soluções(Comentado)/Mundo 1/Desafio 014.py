print('Conversor de Celsius')
tempc = float(input('Qual a temperatura em °C: '))
tempf = (tempc * 9 / 5) + 32  # Fahrenheit = °C x 9/ 5 + 32  
tempk = tempc + 273.15        # Kelvin = °C + 273.15 
print(f'{tempc} ºC \nem fahrenheit {tempf} °F \nem kelvin {tempk} K')
