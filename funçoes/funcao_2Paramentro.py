def quadrado(palavra, numero):
    'função Mostrar na tela quadrado ou cubo'
    if palavra == 'quadrado':
        return print(f'o quadrado de {numero} = {numero**2}')
    elif palavra == 'cubo':
        return print(f'o cubo de {numero} = {numero**3}')
    else:
        print("palavra invalida")

palavra = input("qual opreção deseja realizar, quadrado ou cubo?")
numero = float(input("qual numero deseja realizar a operação"))
quadrado(palavra, numero)
# ou
print(quadrado('quadrado', 2))