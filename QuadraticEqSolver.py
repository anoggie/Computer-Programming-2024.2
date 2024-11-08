# Valores de a, b e c
try:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

# Vê se é uma equação de segundo grau e me avisa
    if a == 0:
        print("Não é uma equação de segundo grau, pois a = 0.")
    else:
        # Calcula o delta
        delta = b**2 - 4 *a*c

        # Verifica se as raízes são reais
        if delta < 0:
            print("A equação não possui raízes reais, bro :/")

        elif delta == 0:
            # Raiz única
            x = -b / (2 * a)
            print("A equação possui uma raiz real: x = ", x)
        else:
            # Duas raízes reais
            x1 = (-b + (delta)**0.5) / (2 * a)
            x2 = (-b - (delta)**0.5) / (2 * a)
            print("A equação possui duas raízes reais: x1 =", x1, "e x2 =", x2)

except ErroValor:
    print("Erro: Te pedi número, não letra >:(")
