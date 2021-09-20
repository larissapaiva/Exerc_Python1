# recebendo valor
x = input('Digite algo: ')
# Mostrando
print(type(x))
# verificando se é numero
print('Ele é numérico: ', x.isnumeric())

# verificando se é letra
print('Ele é alfabético: ', x.isalpha())
# verificando se é alfa-numero
print('Ele é alfa-numérico: ', x.isalnum())
# verificando se é numero real
print('Ele é Decimal: ', x.isdecimal())
# verificando se esta em minusculo
print('Ele é minúsculo: ', x.islower())
# verificando se esta em maisculo
print('Ele é maiúsculo: ', x.isupper())