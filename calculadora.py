print('-----CALCULADORA DE IMC-----')

peso = float(input('Insira o seu peso em KG: '))
altura = float(input('Insira a sua altura em metros: '))

if peso <= 0 or altura <= 0:
    print('insira um valor!')
else:
    imc = peso / (altura ** 2)

IMC = round(imc, 2)
print('O seu IMC é:', IMC)

if IMC < 18.5:
    print('Abaixo do peso')

elif 18.5 <= IMC <= 24.9:
    print('Peso normal')

elif 25 <= IMC <= 29.9:
    print('Sobrepeso')

elif 30 <= IMC <= 34.9:
    print('Obesidade grau 1')

elif 35 <= IMC <= 39.9:
    print('Obesidade grau 2')

elif IMC >= 40:
    print('Obesidade grau 3')
