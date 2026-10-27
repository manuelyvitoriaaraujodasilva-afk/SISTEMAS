# Variaveis para cadastro
nome = ""
idade = ""
usuario = ""
senha = ""
# Apenas a tela de visualizacao

#variaveis para login
login_usuario = "" 
login_senha = ""
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
# Variaveis
    # Se digitar 2, abre a tela de login
    if (opcao == "1") :
        print("========================")
        print("====Tela de Cadastro====")
        print("========================")
        nome = input("Digite o seu nome: ")
        idade = input("Digite sua idade: ")
        usuario = input("Digite o  seu usuario: ")
        senha = input("Digite sua senha: ")
        print("\n Cadastro realizado! \n")
        

        login_usuario = input("Digite o usuario cadastrado") 
    #se digitar 2, abre a tela do login
    elif (opcao == "2") :
        print("========================")
        print("====Tela de login====")
        print("========================")
        login_senha = input("Digite o usuario: ")
        login_senha = input("Digite a senha:")

    #Processamento de usuario e senha
        if login_usuario == usuario  and login_senha == senha :
            while True :
                print("\nLogin realizado com sucesso! \n")
                print("Bem vindo,", nome)
                print("\n=====Area do Usuario=====\n")
                print("1 - ver os dados cadastrados")
                print("2 - Voltar para o menu anterior")

                usuario_opcao = input("\nEscolha uma das opcoes do menu acima: \n")

                if (usuario_opcao == "1"):
                    print("\n=====================")
                    print("===Dados cadastrados===")
                    print("=====================\n")
                    #Mostrar dados do usuario:
                    print("Nome de cadastro:", nome)
                    print("Idade do usuario:",idade)
                    print("Nome do usuario:",usuario)
                    print("Senha do usuario:",senha)

                elif(usuario_opcao == "2"): 
                    print("\nVoce esta voltando para o menu anterior") 
                    break 
                else:
                    print("\nOpcao digitada invalida, use os numeros do Menu!")

           #se nao estiver correto entra nocaso abaixo
        else:
           print("\nUsuario ou senha incorretos\n")

    #se digitar 3, o codigo sai da execucao
    elif (opcao == "3") :
        print("\nVoce esta saindo do cadastro, ate mais!\n")
        break
    #Se nao for 1,2 ou 3, mostrar erro e repetir o codigo
    else :
        print("Valor digitado,invalido, use apenas numeros inteiros no menu")
