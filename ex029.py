# AULA 10 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
# dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
km = float(input('Digite a sua velocidade: '))
if km <= 80:
    print('Você está na velocidade certa! ')
else:
    v = (km-80)*7
    print('Você está acima do limite de velocidade! \nSua multa é de {:.2f} reais '.format(v))
print('Dirija com segurança!')
