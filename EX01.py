1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria: um serviço em que as pessoas 
    possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de 
    assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.
    
    Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:

Nível e Porcentagem sobre o faturamento:

Basic 30%

Silver 20%

Gold 10%

Platinum 5%


Resolução:

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
