#Importar biblioteca
from datetime import date

#Criar classe Tarefa
class Tarefa:
    """
    Representa uma tarefa no sistema.
    """
    def __init__(self, id, titulo, descricao, projeto_id, responsavel_id, categoria_id, prioridade, status, prazo):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.projeto_id = projeto_id
        self.responsavel_id = responsavel_id
        self.categoria_id = categoria_id
        self.prioridade = prioridade
        self.status = status
        self.data_criacao = date.today()
        self.prazo = prazo

    def __str__(self):
        return (f"Tarefa(id={self.id}, titulo={self.titulo}, descricao={self.descricao}, "
                f"projeto_id={self.projeto_id}, responsavel_id={self.responsavel_id}, categoria_id={self.categoria_id}, "
                f"prioridade={self.prioridade}, status={self.status}, data_criacao={self.data_criacao}, prazo={self.prazo})")
