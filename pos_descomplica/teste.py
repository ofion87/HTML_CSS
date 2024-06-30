dataNascimento= int(input("entre com a sua data de nascimento: "))
dataAtual= int(input("entre com o ano atual"))
idade = dataAtual-dataNascimento
print("Qual o seu titulo de eleitor") if idade>=18 else print("informe o RG do responsavel")
