# AULA 10 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = float(input('Qual a distancia da viagem? '))
if km <= 200:
    print('O preço da passagem é de {:.2f} reais'.format(km * 0.50))
else:
    print('O preço da passagem é de {:.2f} reais'.format(km * 0.45))
