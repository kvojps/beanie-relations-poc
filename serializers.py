from pydantic import BaseModel


class UserRequest(BaseModel):
    nome: str
    email: str


class UserResponse(BaseModel):
    titulo: str
    conteudo: str
    autor: str
