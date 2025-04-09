def quadrado(numero = 5):
    'função pra mostrar na tela o quadrado do numero.'
    print(f'o quadrado do {numero} é = {numero ** 2}')

numero = int(input('Digite o numero que você que saber o quadrado: '))
help(quadrado)
quadrado(numero)
# ou
print(quadrado(8))