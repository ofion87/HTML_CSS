# While = enquanto | Ele executa a expressão enquanto a condição for verdadeira.
# Variavel de controle deve contar na expressão

a = 1

while a < 10:
    print("Teste")
    a = a+1


# Laço FOR
# utilização com quantidade determinada de vezes que se repetirá
for b in range(5):
    print("marcio")
#utilização com um df rodando todos os elementos dele
c = ["beltran","Junior","Samuel","André"]
for c in c:
    print(c)
# utilização com quebra de uma string
d = "descomplica"
for d in d:
    print(d)

# utilizando um loço para incrementar valores em um DF

a=[]
b=1
print(a)
while b <=3:
    a.append(input("Digite o nome do aluno: "))
    b = b+1
print(a)


# usando o laço para dar input e output no DF

a = ["Marcio","Bruna","Marcio"]
print("aqui mostramos o DF com as posições originais")
print(a)
print("Utilizamos o metodo insert para incluir um novo elemento no DF. O metodo necessida indicar em qual posição gostariamos de inserir o novo parametro. Nessa situação ele impura os demais registros a partir do indice 0")
a.insert(1,"Hellen")
print(a)
print("Necesse momento utilizaremos o metodo remove para altera o DF e excluir o Registro Marcio do nosso DF. Não existe a necessidade de informar o elemente apenas indicar o nome a ser excluido. Nesse momento ele apenas exclui o primeiro marcio encontrado.")
a.remove("Marcio")
print(a)