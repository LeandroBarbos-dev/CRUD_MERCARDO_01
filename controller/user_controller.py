from model.user_model import User

class UserController:
    def __init__(self, service):
        self.service = service

    def cadastrar(self, user):
        self.service.cadastrar(user)


    def login(self, email, senha):
        return self.service.login(email, senha)
        