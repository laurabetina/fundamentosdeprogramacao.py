#SISTEMA DE MATRÍCULA

idade = int(input("Digite a idade do aluno: "))
media = float(input("Digite a média do aluno: ").replace(",", "."))
freq = float(input("Digite o percentual de frequência do aluno: ").replace("%", "").replace(",", "."))
print("TIPOS DE CURSOS\nTIPO 1 - GRADUAÇÃO")
print("TIPO 2 - TÉCNICO")
print("TIPO 3 - PÓS-GRADUAÇÃO")
opcao = int(input("Selecione o tipo de curso (de 1 à 3): "))


if freq < 75:
  print("ALUNO REPROVADO POR FALTA! ")

else:
  match opcao:
   case 1: 
    if media >= 7 and freq >= 75:
      print("ALUNO APROVADO! ")
    elif media >= 5 and freq >= 75:
      print("ALUNO EM RECUPERAÇÃO! ")
    else:
      print("ALUNO REPROVADO! ")

   case 2: 
    if media >= 6 and freq >=75:
      print("ALUNO APROVADO! ")
    elif media >= 4 and freq >=75:
      print("ALUNO EM RECUPERAÇÃO! ")
    else:
      print("ALUNO REPROVADO! ")

   case 3:
    if media >=7 and freq >=75:
      print("ALUNO APROVADO! ")
    else:
      print("ALUNO REPROVADO! ")


    