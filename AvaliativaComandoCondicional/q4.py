#questão 4 - bissexto checker

try:
# Pede ao usuário para inserir um ano
    x = int(input('Digite um ano:'))
    
# Valida se o ano informado é divisível por 400 e por 4, mas não divisível por 100
    if (x % 400 == 0) or (x % 4 == 0) and (x % 100 !=0):        
            print ('O ano é bissexto.')

# Caso não seja, exibe a mensagem informando ao usuário
    else:
        print('O ano não é bissexto.')

except ValueError:
    print('Erro: Insira um número válido!')