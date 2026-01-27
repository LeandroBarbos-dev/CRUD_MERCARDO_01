import json
from model.user_model import User

CAMINHO = "data/user.json"

class UserRepository:

    def _ler_arquivo(self):
        try:
            with open(CAMINHO, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        
    def _salvar_arquivo(self, dados):
        with open(CAMINHO, "w",encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def _proximo_id(self, dados):
        if not dados:
            return 0
        return max(u["id"] for u in dados) + 1

    def salvar(self, user: User):
        dados = self ._ler_arquivo()

        user.id = self._proximo_id(dados)

        dados.append(user.to_dict())
        self._salvar_arquivo(dados)

    def listar(self):
        dados = self._ler_arquivo()
        return [User(**u) for u in dados]
    
    def login(self, email, senha):
        dados = self._ler_arquivo()
        for u in dados:
            if u["email"] == email and u["senha"] == senha:
                return User(
                    u["id"],
                    u["nome"],
                    u["email"],
                    u["senha"]
                )

        return None

