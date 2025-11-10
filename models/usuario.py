#Criar classe de Usuario
class Usuario:
    def __init__(self, id: int = None, nome: str = None, email: str = None):
        self.id = id
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Usuario(id={self.id}, nome='{self.nome}', email='{self.email}')"
#Tratar o atributo nome(não permitir nomes com menos de 3 caracteres)
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor or len(valor) < 3:
            raise ValueError("Nome muito curto!")
        self._nome = valor


#Tratar o atributo Email(não permitir emails sem @ e sem .)
    @property
    def email(self):
        return self._email


    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            raise ValueError("E-mail inválido. Deve conter '@' e '.'")
        self._email = valor 