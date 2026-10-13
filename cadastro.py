while True:
    print ("===================")
    print ("sistema de cadrastro")
    print ("===================")

    print ("1 - Cadrastar")
    print ("2 - Fazer login")
    print ("3 - Sair")

    opcao = int(input(" Escolha uma opção : "))
#se o usuario digitar 1, vai ser exibido
# a açao abaixo:
    if (opcao == 1) :
        print("========================")
        print("====Tela de Cadastro====")
        print("========================")

    elif (opcao == 2) :
        print("========================")
        print("====Fazer login====")
        print("========================")
    else: 
        print("Voce esta saindo do cadastro, ate mais")
        break

