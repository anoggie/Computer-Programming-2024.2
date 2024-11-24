# Questão 3 - Jogo da advinhação
# Desenvolvido por Anielly e Israel

import random

try:
    sorteado = random.randint(1,100)
    min = 1
    max = 100

    
    # print(sorteado)  <- Um checker para os desenvolvedores validar o funcionamento das condicionais do restante do código

    print('Tente acertar o número sorteado de 1 a 100 em até 4 tentativas. Boa sorte!')

    # Primeira tentativa
    tentativa1 = int(input('Tentativa 1/4: '))

    # Se acertasse o número de primeira
    if tentativa1 == sorteado:
        print('Muito bem! Você acertou de primeira! Se tu jogar na mega da virada, tu ganha!')

    else:
        # Se a tentativa for um valor menor que o sorteado...
        if tentativa1 < sorteado:
            # O intervalo mínimo vai ser a tentativa + 1
            min = tentativa1 + 1
            print('O número sorteado é maior. O intervalo está entre', min, 'e', max)
        # Caso contrário: tentativa - 1
        elif tentativa1 > sorteado:
            max = tentativa1 - 1
            print('O número sorteado é maior. O intervalo está entre', min, 'e', max)
        
        # Segunda tentativa
        # A partir daqui, a lógica é a mesma, e vai se repetindo até a última!
        tentativa2 = int(input('Tentativa 2/4: '))
        if tentativa2 == sorteado:
            print('Muito bem! Você acertou na segunda tentativa!')
        else:
            if tentativa2 < sorteado:
                min = tentativa2 + 1
                print('O número sorteado é maior. O intervalo está entre', min, 'e', max)
            elif tentativa2 > sorteado:
                max = tentativa2 - 1
                print('O número sorteado é maior. O intervalo está entre', min, 'e', max)

            # Terceira tentativa
            tentativa3 = int(input('Tentativa 3/4: '))
            if tentativa3 == sorteado:
                print('Muito bem! Você acertou na terceira tentativa!')
            else:
                if tentativa3 < sorteado:
                    min = tentativa3 + 1
                    print('O número sorteado é maior. O intervalo está entre', min, 'e', max)
                elif tentativa3 > sorteado:
                    max = tentativa3 - 1
                    print('O número sorteado é maior. O intervalo está entre', min, 'e', max)

                # Quarta tentativa
                tentativa4 = int(input('Tentativa 4/4: '))
                if tentativa4 == sorteado:
                    print('Quase que não acertava, hein!? Mandou bem!')

                # Neste último caso, se o usuário não acertar nenhuma vez, exibirá o número sorteado.
                else:
                    print('Você não acertou o número. O sorteado era:', sorteado)



except ValueError:
    print('Erro: Insira apenas números inteiros!')
