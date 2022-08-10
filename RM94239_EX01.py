nivel_assinatura_cliente = input("Por favor, informar se o nível da sua assinatura é o BASIC, SILVER, GOLD ou PLATINUM: ")
faturamento_anual_cliente = float(input("Por favor, informar o valor do seu faturamento anual: "))

if nivel_assinatura_cliente.upper() == "BASIC":
    valor_bonus = faturamento_anual_cliente*0.30
    print ("O valor do Bônus a receber do Cliente é de R$ {0:.2f}" .format(valor_bonus))
elif nivel_assinatura_cliente.upper() == "SILVER":
    valor_bonus = faturamento_anual_cliente*0.20
    print ("O valor do Bônus a receber do Cliente é de R$ {0:.2f}" .format(valor_bonus))
elif nivel_assinatura_cliente.upper() == "GOLD":
    valor_bonus = faturamento_anual_cliente*0.10
    print ("O valor do Bônus a receber do Cliente é de R$ {0:.2f}" .format(valor_bonus))
elif nivel_assinatura_cliente.upper() == "PLATINUM":
    valor_bonus = faturamento_anual_cliente*0.05
    print ("O valor do Bônus a receber do Cliente é de R$ {0:.2f}" .format(valor_bonus))
else:
    print ("O nível da assinatura informada é invalido!")
