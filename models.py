from beanie import Document


class User(Document):
    nome: str
    email: str


class Post(Document):
    titulo: str
    conteudo: str
    # relação com autor
