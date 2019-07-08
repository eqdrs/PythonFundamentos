# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

op = 1

while(op != 5):
    print("\n******************* Python Calculator *******************")

    op = int(input("\n\nSelecione o número da operação desejada:\n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\
                    \n4 - Divisão\n5 - Sair\n\nDigite sua opção(1/2/3/4/5): "))
    if(op != 5):
        first_num = int(input("\nPrimeiro número: "))

        second_num = int(input("\n\nSegundo número: "))

        if(op == 1):
            result = first_num + second_num
        elif(op == 2):
            result = first_num - second_num
        elif(op == 3):
            result = first_num * second_num
        else:
            result = first_num / second_num

        print("O resultado é: %s" % (result))



