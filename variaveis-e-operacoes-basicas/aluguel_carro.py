"""
Escreva um programa que leia (na execução) a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa $ 60,00 por dia e $ 0,15 por km rodado.
"""

custo_por_dia = 60
custo_por_kilometro = 0.15

print('Digite as informações referente ao aluguel do veículo')

kilometros_percorridos = float(input('Distância percorrida com o veículo (em Km): '))
dias_alugado = float(input('Período de locação do veículo (em dias): '))

custo_aluguel = (dias_alugado * custo_por_dia) + (kilometros_percorridos * custo_por_kilometro)

print(f'\nCom base nas informações digitadas o custo total do aluguel é $ {custo_aluguel}')