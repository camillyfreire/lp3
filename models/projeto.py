#Criar classe do Projeto
class Projeto:
    def __init__(self, id: int, nome: str, descricao: str):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    def __str__(self):
        return f"Projeto(id={self.id}, nome='{self.nome}', descricao='{self.descricao}')"

#Tratar o atributo nome(não permitir nomes com menos de 3 caracteres)
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor or len(valor) < 3:
            raise ValueError("Nome muito curto!")
        self._nome = valor
