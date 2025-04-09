def temperatura(C):
    'função para mostrar e converter a temperatura de fahrenheit para celsius'
    celsius = (C - 32) * 5/9
    print(f'{celsius:.2f}')
temperatura_F = float(input("Qual a temperatura em fahrenheit? "))
temperatura(temperatura_F)
# ou
print(temperatura(40))
