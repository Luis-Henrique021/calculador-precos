import math

NOME_PRODUTO = input("Digite o nome do produto: ")
valor_avista = float(input("Agora, digite o valor do produto à vista: R$"))
valor_total_parcelado = float(input("Digite o valor do produto parcelado (montante total): R$"))
qtd_parcelas = int(input("Por fim, digite a quantidade de parcelas: "))

diferenca_valor = valor_total_parcelado - valor_avista # diferença dos valores (parcelado e a vista)
valor_por_parcela = valor_total_parcelado / qtd_parcelas # valor por parcela
juros_credito = (diferenca_valor / valor_avista) * 100 # juros total do valor

print(f"{NOME_PRODUTO} -- Valor à vista: R${valor_avista} -- Valor Parcelado {valor_total_parcelado} -- Quantidade de parcelas: {qtd_parcelas}")
print(f"A diferença do valor parcelado e à vista: R${diferenca_valor} -- Valor por parcela: R${valor_por_parcela:.2f} -- Juros (%){juros_credito:.2f}")