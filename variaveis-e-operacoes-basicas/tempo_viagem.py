"""
Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e
a velocidade média esperada para a viagem.
"""

print('Digite a velocidade média da viagem em Km/h e a velocidade a ser percorrida em Km')

distancia = float(input('Distância a percorrer: '))
velocidade_media = float(input('Velocidade média: '))

tempo_de_viagem = velocidade_media / distancia

print(f'\nCom base nas informaçõe o tempo de viagem será {tempo_de_viagem} h.')