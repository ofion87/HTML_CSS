# nome = input("digite seu nome:")
# nascimento = input("Qual o seu ano de nascimento?")
# email = input("digite seu e-mail")
# print("Nome: ",nome)
# print("Data de Nascimento:", nascimento)
# print("e-mail:", email)
a = float(input("digite um número"))
print(a+10)


# Operadores
#     Aritimeticos
#       + - * /
#     Logico
#       <>
#     Relacionais

# Operadores especiais
# Potencia
a = 2
b = 3
print(a**b)
# Raiz quadadta
from cmath import sqrt

print(sqrt(4))

# Resto da divisão

print(18%4)

# IF e ELSE Condição quanto tem mais de um saida

# Ternario só quanto tem duas saidas


idade = int(input("entre com sua idade"))
print("é maior de idade") if idade >= 18 else print("É menor")


# Switch Case(Match)
a = "Marcio"

match a:
    case "Antonio":
        print("não é marcio")
    case "Marcio":
        print("oie Marcio")
    case "José":
        print("Fala Zé")