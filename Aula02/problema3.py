idade = int(input("Digite a idade: "))
t_contribuicao = int(input("Digite o tempo de contribuição: "))
sex = input("Digite o sexo (M/F): ")

if (idade>=65 and sex == "M") or (idade>=60 and sex == "F") or (idade>=60 and t_contribuicao>=35 and sex == "M") or (idade>=55 and t_contribuicao>=30 and sex == "F"):
    print("Sim")
else:
    print("Não")
