# Recebe um número de 4 algarismos do usuário
numero = int(input("Digite um número de 4 algarismos: "))

# Separa cada algarismo usando divisões e módulos
a = numero // 1000         # 1meiro
b = (numero // 100) % 10   # 2gundo
c = (numero // 10) % 10    # 3ceiro
d = numero % 10            # último

# Se imaginarmos uma reta de A até D, temos três possibilidades de A ser maior que B, C e/ou D...
# Então, precisamos inverter isso, fazendo com que A seja menor que todos.
# Portanto:
if a > b:
    x = a # Isso aq faz uma variável 'temporária', que vai ser usada para receber o valor de A, e comutar o valor para que B > A
    a = b # A vai receber o valor de B
    b = x # O valor de B vai ser comutado pelo de A :p
if a > c:
    x = a
    a = c # Same energy da ocasião anterior ><
    c = x
if a > d:
    x = a
    a = d
    d = x

# De B até D, são duas possibilidades:
if b > c:
    x = b
    b = c
    c = x
if b > d:
    x = b
    b = d
    d = x

# E de C até D, uma ocasião:
if c > d:
    x = c
    c = d
    d = x

# Exibe tudo em ordem crescente :D
print("Algarismos em ordem crescente:", a, b, c, d)
