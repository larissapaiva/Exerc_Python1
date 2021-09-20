# AULA 7 - Escreva um programa que converta uma temperatura digitada em graus Celsius e converta para graus Fahrenheit.
c = float(input('Digite a temperatura em °C: '))
print('{}°C equivalem a {:.2f}°F e {:.2f}°K'.format(c, ((1.8 * c) + 32), (c + 273)))
