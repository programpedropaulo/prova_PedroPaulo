import random
valor = True
print("")
print("Olá me chamo Lino! Vamos começar nossa brincadeira")
print("")
nome = input("Gostaria de te conhecer, então por favor me diga seu nome: ")
print("Prazer em te conhecer, ", nome)
print("")
print("Adivinhe o número se puder! ")
print("")
while valor == True:
    numeroAleatorio = random.randint(0,100)
    print("Número para teste ", numeroAleatorio )
    contador = 0
    while contador <= 9:
        print("tentativa:", contador)
        numeroInserido = int(input("Insira um número: "))
        if numeroAleatorio == numeroInserido:
            print("Parabens voce acertou! o número era " ,numeroAleatorio)
            contador = 9

        elif numeroInserido < numeroAleatorio:
            print("Dica: Aumente o número mais um pouco! ")
        elif numeroInserido >  numeroAleatorio:
            print("Dica: Abaixe um pouco mais")
     
            
        contador += 1
    print("reinicializar o jogo")
    opcao = int(input("Digite 1 para comecar outro jogo ou 0 para Sair:"))
    if opcao == 0:
        valor = False