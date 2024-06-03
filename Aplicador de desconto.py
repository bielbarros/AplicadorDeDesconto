print('Bem vindo a loja do Gabriel Barros!')
produtov = float(input("Entre com o valor do produto:"))

produtoq = int(input("Entre com a quantidade do produto:"))

resultado = produtov * produtoq
valor_sem_desconto = resultado  # Armazena o valor sem desconto inicialmente

if 2500 <= resultado < 6000:
    resultado_com_desconto = resultado * 0.96
    print(f"Valor com desconto de 4% aplicado: R${resultado_com_desconto:.2f}")
    valor_sem_desconto = resultado  

elif 6000 <= resultado < 10000:
    resultado_com_desconto = resultado * 0.93
    print(f"Valor com desconto de 7% aplicado: R${resultado_com_desconto:.2f}")

elif resultado >= 10000:
    resultado_com_desconto = resultado * 0.89
    print(f"Valor com desconto de 11% aplicado: R${resultado_com_desconto:.2f}")

else:
    resultado_com_desconto = resultado  # Não houve desconto
    print(f"Valor total: R${resultado:.2f}")

# Valor sem desconto
print(f"Valor sem desconto: R${valor_sem_desconto:.2f}")