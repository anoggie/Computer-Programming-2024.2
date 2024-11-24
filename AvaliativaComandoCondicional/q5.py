# Questão 5 - Calculador de dia juliano com base em uma data válida.
# Desenvolvido por Anielly e Israel

try:

    # Pede as informações da data ao usuário
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    # Impede que o usuário insira valores negativos
    if dia < 0 or mes < 0 or ano < 0:
        print("Erro: Não insira valores negativos!")
    else:

    # Utilizando como base a q4, aqui o programa verifica se o ano é bissexto
        bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

        # Determinando se o mês vai até 31
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            dias_mes = 31

        # Caso especial de fevereiro
        elif mes == 2:
            if bissexto:
                dias_mes = 29
            else:
                dias_mes = 28

        # Determinando se o mês vai até 30
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            dias_mes = 30

        else:
            dias_mes = 0

        # Checker para ver se a data é válida ou não
        if mes < 1 or mes > 12 or dia < 1 or dia > dias_mes:
            print('Erro: Data inválida!')
        else:
            # Caso a data seja válida, calcula o dia juliano
            dia_juli = dia

            if mes > 1:
                dia_juli = dia_juli + 31

            # Em fevereiro, verifica se o ano é bissexto e caos positivo, soma 29, caso não, soma 28
            if mes > 2:
                if bissexto:
                    dia_juli = dia_juli + 29
                else:
                    dia_juli = dia_juli + 28

            # Março a Novembro
            if mes > 3:
                dia_juli = dia_juli + 31
            if mes > 4:
                dia_juli = dia_juli + 30 
            if mes > 5:
                dia_juli = dia_juli + 31
            if mes > 6:
                dia_juli = dia_juli + 30  
            if mes > 7:
                dia_juli = dia_juli + 31
            if mes > 8:
                dia_juli = dia_juli + 31
            if mes > 9:
                dia_juli = dia_juli + 30
            if mes > 10:
                dia_juli = dia_juli + 31
            if mes > 11:
                dia_juli = dia_juli + 30


            # Exibe a data em dia juliano para o usuário
            print('A data', dia,'/', mes, '/' ,ano, 'corresponde ao dia juliano:', dia_juli)


except ValueError:
    print('Erro: Insira apenas números!')
