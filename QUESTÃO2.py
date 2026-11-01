#CLASSIFICAÇÃO DO PRODUTO

preço = float(input("Digite o preço do produto em R$: ").replace(",", "."))
qntd = int(input("Quantidade do produto em estoque: "))

if preço <= 0:
    print ("PREÇO INVÁLIDO")

if qntd < 0:
    print ("QUANTIDADE INVÁLIDA")

elif preço > 1000 and qntd < 5:
    print ("PRODUTO CARO COM ESTOQUE CRÍTICO")

elif preço >1000 and qntd <= 20:
 print("PRODUTO CARO COM ESTOQUE NORMAL")

elif preço >1000 and qntd > 20:
   print("PRODUTO CARO COM ESTOQUE NORMAL")

elif preço <=1000 and qntd < 5:
   print("ESTOQUE CRÍTICO")

else:
   print ("ESTOQUE NORMAL")

print(f"Preço: R$ {preço:.2f}")


