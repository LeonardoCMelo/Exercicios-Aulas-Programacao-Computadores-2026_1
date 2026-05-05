nome = input("Nome completo do aluno: ").upper().split()

login = ""

login = nome[0]
for n in nome[1:len(nome)-1]:
    login += n[0]
login += nome[len(nome)-1]

print(f"Login: {login}")