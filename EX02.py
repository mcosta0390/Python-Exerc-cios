2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives. Desenvolva um programa em que 
o usuário informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, 
verifique e exiba qual dia foi o escolhido.



Resolução:

votacao1 = input("Por favor, escolha qual o melhor dia para efetuarmos a realização da nossa Live: SEGUNDA, TERÇA, QUARTA, QUINTA ou SEXTA? ")
votacao2 = input("Por favor, escolha qual o melhor dia para efetuarmos a realização da nossa Live: SEGUNDA, TERÇA, QUARTA, QUINTA ou SEXTA? ")
votacao3 = input("Por favor, escolha qual o melhor dia para efetuarmos a realização da nossa Live: SEGUNDA, TERÇA, QUARTA, QUINTA ou SEXTA? ")
votacao4 = input("Por favor, escolha qual o melhor dia para efetuarmos a realização da nossa Live: SEGUNDA, TERÇA, QUARTA, QUINTA ou SEXTA? ")
votacao5 = input("Por favor, escolha qual o melhor dia para efetuarmos a realização da nossa Live: SEGUNDA, TERÇA, QUARTA, QUINTA ou SEXTA? ")

segunda = 0
terça = 0
quarta = 0
quinta = 0
sexta = 0

if votacao1.upper() == "SEGUNDA":
    segunda = segunda + 1
elif votacao1.upper() == "TERÇA":
    terça = terça + 1
elif votacao1.upper() == "QUARTA":
    quarta = quarta + 1
elif votacao1.upper() == "QUINTA":
    quinta = quinta + 1
elif votacao1.upper() == "SEXTA":
    sexta = sexta + 1
else:
    print ("O dia informado não é valido!")
if votacao2.upper() == "SEGUNDA":
    segunda = segunda + 1
elif votacao2.upper() == "TERÇA":
    terça = terça + 1
elif votacao2.upper() == "QUARTA":
    quarta = quarta + 1
elif votacao2.upper() == "QUINTA":
    quinta = quinta + 1
elif votacao2.upper() == "SEXTA":
    sexta = sexta + 1
else:
    print ("O dia informado não é valido!")
if votacao3.upper() == "SEGUNDA":
    segunda = segunda + 1
elif votacao3.upper() == "TERÇA":
    terça = terça + 1
elif votacao3.upper() == "QUARTA":
    quarta = quarta + 1
elif votacao3.upper() == "QUINTA":
    quinta = quinta + 1
elif votacao3.upper() == "SEXTA":
    sexta = sexta + 1
else:
    print ("O dia informado não é valido!")
if votacao4.upper() == "SEGUNDA":
    segunda = segunda + 1
elif votacao4.upper() == "TERÇA":
    terça = terça + 1
elif votacao4.upper() == "QUARTA":
    quarta = quarta + 1
elif votacao4.upper() == "QUINTA":
    quinta = quinta + 1
elif votacao4.upper() == "SEXTA":
    sexta = sexta + 1
else:
    print ("O dia informado não é valido!")
if votacao5.upper() == "SEGUNDA":
    segunda = segunda + 1
elif votacao5.upper() == "TERÇA":
    terça = terça + 1
elif votacao5.upper() == "QUARTA":
    quarta = quarta + 1
elif votacao5.upper() == "QUINTA":
    quinta = quinta + 1
elif votacao5.upper() == "SEXTA":
    sexta = sexta + 1
else:
    print ("O dia informado não é valido!")


print("O total dos votos referente aos dias foram:\nSEGUNDA {}\nTERÇA {}\nQUARTA {}\nQUINTA {}\nSEXTA {}\n" .format(segunda, terça, quarta, quinta, sexta))

if segunda > terça and segunda > quarta and segunda > quinta and segunda > sexta:
    print ("O dia escolhido para a realização da nossa Live foi na segunda-feira, com o total de {} votos!" . format (segunda))
elif terça > segunda and terça > quarta and terça > quinta and terça > sexta:
    print ("O dia escolhido para a realização da nossa Live foi na terça-feira, com o total de {} votos!" . format (terça))
elif quarta > segunda and quarta > terça and quarta > quinta and quarta > sexta:
    print ("O dia escolhido para a realização da nossa Live foi na quarta-feira, com o total de {} votos!" . format (quarta))
elif quinta > segunda and quinta > terça and quinta > quarta and quinta > sexta:
    print ("O dia escolhido para a realização da nossa Live foi na quinta-feira, com o total de {} votos!" . format (quinta))
elif sexta > segunda and sexta > terça and sexta > quarta and sexta > quinta:
    print ("O dia escolhido para a realização da nossa Live foi na sexta-feira, com o total de {} votos!" . format (sexta))
else:
    print ("Houve um impate na contagem da votação. Favor entrar em contato com a direção!")


