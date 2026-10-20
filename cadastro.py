while True:
    print ("===================")
    print ("sistema de cadrastro")
    print ("===================")

    print ("1 - Cadrastar")
    print ("2 - Fazer login")
    print ("3 - Sair")

    opcao = input(" Escolha uma opcao : ")
    #funcionalidades
#se o usuario digitar 1, vai ser exibido
# a acao abaixo:
    if (opcao == "1") :
        print("========================")
        print("====Tela de Cadastro====")
        print("========================")

    elif (opcao == "2") :
        print("========================")
        print("====Fazer login====")
        print("========================")
    #se digitar 3, o codigo sai da ezecucao
    elif (opcao == "3") :
        print("Voce esta saindo do cadastro, ate mais")
        break
#ae nao for 1,2 ou 3, mostrar erro e repetir o codigo
    else :
        print("Valor digitado,invalido, use apenas numeros inteiros no menu")
