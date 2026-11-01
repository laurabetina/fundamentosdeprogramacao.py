#CLASSIFICAÇÃO DE DESEMPENHO

produt = float(input("Digite a nota de PRODUTIVIDADE: ").replace(",", "."))
qualidade = float(input("Digite a nota de QUALIDADE: ").replace(",", "."))
presenca = float(input("Digite o PERCENTUAL DE PRESENÇA: ").replace("%", "").replace(",", "."))
media = (qualidade + produt/2)

if presenca < 75:
   print("Desempenho comprometido por baixa frequência ")

elif media >= 9 and presenca >= 90:
   print("EXCELENTE ")

elif media >=7 and presenca >= 85: 
   print("BOM")

elif media >= 5 and presenca >= 75:
   print("REGULAR")

else:
   print("INSATISFATÓRIO")

