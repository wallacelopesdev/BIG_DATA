
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]
print(f'pares: {pares}')
print(f'impares: {impares}')
