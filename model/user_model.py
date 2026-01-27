class User:
    def __init__(self, id, nome, email, senha, cargo):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo

    def to_dict(self):
        return {
            "id": self.id,
            "nome":self.nome,
            "email": self.email,
            "senha": self.senha,
            "cargo": self.cargo
        }