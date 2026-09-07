#Entrada de dados 
total_compra = float(input("digite o valor total da compra:"))

#condições para desconto
if total_compra < 200:
    print("você recebeu 5% de desconto:")
    desconto = total_compra *0.05
    print("Valor final:", desconto) 
elif total_compra >=200 and total_compra <300:
    desconto = total_compra *0.10
else:
    desconto = total_compra *0.15

# Cálculo do valor final
valor_final = total_compra - desconto

# Saída de dados
print(f"Valor da compra: R$ {total_compra:.2f}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_final:.2f}")