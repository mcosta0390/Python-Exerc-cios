3 – Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa razão, a escola de inglês 
JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito:
   o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm
   número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior 
   nota.

Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas deve ser exibida uma mensagem no seguinte
padrão:

VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.




Resolução:

soma1 = 0
quantidade1 = 0

for x in range (1,51,2):
   nota1 = float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES. POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: " .format(x)))
   soma1 = soma1 + nota1
   quantidade1 = quantidade1 + 1

print ("A quantidade de alunos ímpares foi de {}, e a soma das notas desses alunos foi de {}" .format (quantidade1, soma1))

media_alunos_impares = soma1 / quantidade1

print ("A média das notas dos alunos ímpares foi de {}" .format(media_alunos_impares))


soma2 = 0
quantidade2 = 0

for y in range (2,51,2):
   nota2 = float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES. POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: " .format(y)))
   soma2 = soma2 + nota2
   quantidade2 = quantidade2 + 1

print ("A quantidade de alunos pares foi de {}, e a soma das notas desses alunos foi de {}" .format (quantidade2, soma2))

media_alunos_pares = soma2 / quantidade2

print ("A média das notas dos alunos pares foi de {}" .format(media_alunos_pares))


if media_alunos_impares > media_alunos_pares:
    print ("Alunos ímpares alcaçaram o maior valor da nota, com {} de média." .format (media_alunos_impares))
else:
    print("Alunos pares alcaçaram o maior valor da nota, com {} de média.".format(media_alunos_pares))


