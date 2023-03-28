"""
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário (na chamada).
Calcule o total em segundos.
"""

print('Digite a quantidade de dias, horas, minutos e segundos')

horas = float(input('Horas: '))
minutos = float(input('Minutos: '))
segundos = float(input('Segundos: '))

tempo_total = (horas * 3600) + (minutos * 60) + segundos

print(f'\nO tempo total em segundos é {tempo_total} s.')