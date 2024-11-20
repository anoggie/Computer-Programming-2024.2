# Questão 1 - Calculadora de IMC
# Desenvolvido por Anielly e Israel

# Proteção do código de possíveis erros do usuário.
try:

    # Pede para o usuário digitar o peso em kg
    peso = float(input('Digite o seu peso (kg): '))

    # Pede a altura em cm
    alturaCm = float(input('Altura (cm): '))

    # Conversão de altura de cm para metros
    alturaM = alturaCm / 100

    # Fórmula para calcular o IMC, arredondando 1 casa decimal
    imc = round((peso / (alturaM)**2), 1)

    # Condicionais e classificações com base no IMC
    if imc < 18.5:
        situacao = 'Abaixo do normal'
    elif 18.5 <= imc < 24.9:
        situacao = 'Normal'
    elif 25.0 <= imc < 29.9:
        situacao = 'Sobrepeso'
    elif 30.0 <= imc < 34.9:
        situacao = 'Obesidade grau I'
    elif 35.0 <= imc < 39.9:
        situacao = 'Obesidade grau II'

    else:  # Para IMC maior ou igual a 40.0
        situacao = print('Obesidade grau III')

    # Retorna com o IMC calculado e a situação
    print('Seu IMC é:', imc, '; Sua situação:', situacao)

# Mensagem de erro para erros de digitação
except ValueError:
    print('Erro: Valores informados inválidos. Peso e altura devem ser números.')
