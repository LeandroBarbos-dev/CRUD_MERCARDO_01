from model.user_model import User

class UserController:
    def __init__(self, service):
        self.service = service

    def cadastrar(self, nome, email, senha, cargo):
        self.service.cadastrar(nome, email, senha, cargo)


    def login(self, email, senha):
        return self.service.login(email, senha)
        