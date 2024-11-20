# Questão 2 - Calculadora de nota IFRN
# Desenvolvido por Anielly e Israel

try:
    # Pede ao usuário informar as notas das duas etapas do semestre.
    n1 = int(input('Insira sua nota da etapa 1: '))
    
    # Valida se a nota está dentro do intervalo permitido.
    if n1 < 0 or n1 > 100:
        print('A nota deve estar entre 0 e 100!')
    else:
        n2 = int(input('Insira sua nota da etapa 2: '))
        if n2 < 0 or n2 > 100:
            print('A nota deve estar entre 0 e 100!')
        else:
            # Calcula a média
            media = int((n1 * 2 + n2 * 3) / 5)

            if media >= 60:
                print('Média:', media)
                print('Aprovado(a)! Parabéns!')
            # Verifica se foi para avaliação final
            elif media >= 20:  
                print('Sua média foi:', media, 'portanto, fará avaliação final.')
                nfinal = int(input('Insira sua nota na avaliação final: '))
                
                # Calcula a média final
                mfinal = (media + nfinal) / 2
                if mfinal >= 60:
                    print('Média final:', mfinal, 'Aprovado(a)!')
                else:
                    print('Média final:', mfinal, 'Reprovado(a)!')
            else:
                print('Média:', media, 'Reprovado(a) diretamente.')
except ValueError:
    print('Por favor, insira um número válido.')
