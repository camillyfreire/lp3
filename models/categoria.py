#Criar classe de Categoria
class Categoria:
    def __init__(self, id: int = None, nome: str = None):
        self.id = id
        self.nome = nome

#Tratar o atributo nome(não permitir nomes com menos de 3 caracteres)
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor or len(valor) < 3:
            raise ValueError("Nome muito curto!")
        self._nome = valor

    def __str__(self):
        return f"Categoria(id={self.id}, nome='{self.nome}')"