# dados do usuario
nome = ""
idade = ""
usuario = ""
senha = ""

#variaveis para login
login_usuario = "" 
login_senha = ""

#Variaveis de controle
controle_cadastro = ""

#Apenas tela de visualizacao
while True:
    controle_cadastro = "2"
    #alterando o controle cadastro para poder cadastrar quantas vezes quiser,alteracao acima.
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
         while controle_cadastro != "1":
            print("========================")
            print("====Tela de Cadastro====")
            print("========================")
            nome = input("Digite o seu nome: ")
            idade = input("Digite sua idade: ")
            usuario = input("Digite o  seu usuario: ")
            senha = input("Digite sua senha: ")

            controle_cadastro = input("\n Voce deseja valtar para a tela anterior ?\n 1)-Voltar para o menu anterior;\nDigite qualquer tecla para refazer o cadastro;\n")

            if(controle_cadastro == "1"):
             print("\n Cadastro realizado! \n")
            else:
                print("valor digitado invalido, faca o cadastro novamente")
    #se digitar 2, abre a tela do login
    elif (opcao == "2") :
        print("========================")
        print("====Tela de login====")
        print("========================")
        login_usuario = input("Digite o usuario: ")
        login_senha = input("Digite a senha:")

    #Processamento de usuario e senha
        if login_usuario == usuario  and login_senha == senha :
            while True :
                print("\nLogin realizado com sucesso! \n")
                print("Bem vindo,", nome)
                print("\n=====Area do Usuario=====\n")
                print("1 - ver os dados cadastrados")
                print("2 - Voltar para o menu anterior")
                print("3 - Alterar senha")

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
                elif(usuario_opcao == "3"):
                    senha = input ("\nDigite a nova senha: ")
                    
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
