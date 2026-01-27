from view.viewInicio import ViewInicio
from model.user_model import User
from controller.user_controller import UserController
from service.user_service import UserService
from repository.user_repository import UserRepository


userRepository = UserRepository()
userService = UserService(userRepository)
userController = UserController(userService)
viewInicio = ViewInicio()

def menu(usuarioAtual):
    print ("Menu de escolhas".center(30, "-"))
    print(f"Bem vindo {usuarioAtual.nome}!!!")
    


def logar():
    while True:
        op = int(viewInicio.entrar())

        
        match op:
            case 1:#login
                email, senha = viewInicio.login()
        
                if email is not None and senha is not None:
                    user = userController.login(email, senha)
                    print(user.nome)
                    if user is None:
                        print("Email ou senha inválidos")
                    else:
                        print(user.nome)
                        return user
                    
            case 2:#cadastro
                nome, email, senha = viewInicio.cadastrar()
        
                if nome is not None and email is not None and senha is not None:
                    userController.cadastrar(nome, email, senha)
            case 3:
                return "SAIR"
            case _: 
                print("Opção invalida")

def main():
    usuarioAtual = None
    print("Projeto mercadinho")
    while True:
        resultado = logar()

        if resultado == "SAIR":
            break

        if resultado is not None:
            usuarioAtual = resultado
            menu(usuarioAtual)
            break


    

       
if __name__ == "__main__":
    main()

        
    
