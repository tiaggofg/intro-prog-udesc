"""
Escreva um programa que converta uma temperatura dada em °C para °F
"""

temperatura_em_celsius = float(input('Digite a temperatura em graus Celsius que deseja converter para graus Farenheint: '))

temperatura_em_farenheint = (1.8 * temperatura_em_celsius) + 32

print(f'\nA temperatura {temperatura_em_celsius} °C é igual a {temperatura_em_farenheint} °F')