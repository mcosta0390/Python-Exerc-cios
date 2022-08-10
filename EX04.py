minuto_atual = int(input("Por favor, informe o valor do minuto exibido na tela da sua máquina: "))

f = 1

for i in range (1, minuto_atual +1):
    f = f * i

print ("A senha para efetuar o acesso na sua máquina será: LIBERDADE{}" .format(f))








