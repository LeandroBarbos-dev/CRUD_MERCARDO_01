from model.user_model import User

class UserService:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar(self, user):
        if not user.nome:
            raise ValueError("Nome não pode ser vazio")

        if not user.senha:
            raise ValueError("Senha inválida")

        if "@" not in user.email:
            raise ValueError("Email inválido")
        
        self.repository.salvar(user)

    def login(self, email, senha):
        if not senha:
            raise ValueError("Senha inválida")

        if "@" not in email:
            raise ValueError("Email inválido")
        
        return self.repository.login(email, senha)

    