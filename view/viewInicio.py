

class ViewInicio:

    def entrar(self):
        print("Login".center(26, "-"))
        print("1 - Logar".center(26))
        print("2 - Cadastrar".center(26))
        print("3 - Sair".center(26))
        op = 0

        while op<1 or op>3:
            op = int(input())

        return op

    def cadastrar(self):
        nome = ""
        email = ""
        senha = ""
        cargo = 0
        while True:
            print("Cadastro".center(26, "-"))
            
            print(f"1 - Insira seu nome:{nome}")
            print(f"2 - Insira seu email:{email}")
            print(f"3- Insira sua senha:{senha}")
            print(f"4- Insira sua senha:{senha}")
            print(f"5- Concluir")
            print(f"6- Cancelar")

            op = int(input())

            match op:
                case 1:#nome
                    nome = input("Insira seu nome:")
                case 2:#email
                    email = input("Insira seu email:")
                case 3:#senha
                    senha = input("Insira sua senha:")
                case 4:#concluir
                    true = True
                    while true:
                        cargo = input("Insira seu cargo(1- Funcionario / 2- Cliente):")
                        if cargo == 1 or cargo ==2:
                            true = False
                            
                case 5:#concluir
                    if not nome:
                        print("Nome invalido")
                    elif not email or "@" not in email:
                        print("Email invalido")
                    elif not senha:
                        print("Senha invalida")
                    else:
                        return (nome, email, senha)
                case 6:#cancelar
                    break
                case _: 
                    print("Opção invalida")


    def login(self):
        email = ""
        senha = ""
        while True:
            print("Login".center(26, "-"))
            
            print(f"1 - Insira seu email:{email}")
            print(f"2- Insira sua senha:{senha}")
            print(f"3- Concluir")
            print(f"4- Cancelar")

            op = int(input())

            match op:
                case 1:#email
                    email = input("Insira seu email:")
                case 2:#senha
                    senha = input("Insira sua senha:")
                case 3:#concluir
                    if not email or "@" not in email:
                        print("Email invalido")
                    elif not senha:
                        print("Senha invalida")
                    else:
                        return (email, senha)
                case 4:#cancelar
                    break
                case _: 
                    print("Opção invalida")
        
        

    
        