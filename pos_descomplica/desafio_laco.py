# Desenvolver algoritimo:
# Diretor tem necessidade de incluir a lista de alunos
# Os dados necessarios dos alunos serão 
# Nome, CPF, Email, Matricula.
# Para cada aluno o processor necessita tirar a média. Se a média atingir 6 ele deve dar o indicativo de aprovação.
# Listar dados do aluno.
nome=[]
cpf=[]
email=[]
matricula=[]
nota=[]
i=0
a=0
a=int(input("Diretor gostaria de incluir um novo aluno? digite 1 para sim e 0 para não: "))
while a > 0:
    nome.append(input("Nome: ")) 
    cpf.append(input("Entre com o CPF do aluno: "))
    email.append(input("Entre com o e-mail do Aluno: "))
    matricula.append(input("Entre com a matricula do Aluno: "))
    for i in range(3):
        nota.append(int(input("Entre com a nota")))
        print(nota)
        if i >= 2:
            media=(nota[0]+nota[1]+nota[2])/(i+1)
            if media >= 6:
                    print("parabens você está formado com a nota ",media)
                    i= 0
                    nota.clear()
            else: 
                print("Você repetiu de ano com a nota", media)
                i=0
                nota.clear()
        i= i+1
    a = int(input("Diretor gostaria de incluir um novo aluno? digite1 para sim e 0 para não: "))
print("Muito obrigado")                    
