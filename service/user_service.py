from model.user_model import User

class UserService:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar(self, nome, email, senha, cargo):
        if not nome:
            raise ValueError("Nome não pode ser vazio")

        if not senha:
            raise ValueError("Senha inválida")

        if "@" not in email:
            raise ValueError("Email inválido")
        
        if not cargo:
            raise ValueError("Cargo invalido")
        
        user = User(0, nome, email, senha, cargo)
        
        self.repository.salvar(user)

    def login(self, email, senha):
        if not senha:
            raise ValueError("Senha inválida")

        if "@" not in email:
            raise ValueError("Email inválido")
        
        return self.repository.login(email, senha)

    