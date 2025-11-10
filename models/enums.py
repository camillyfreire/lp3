from enum import Enum

class Prioridade(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3

class Status(Enum):
    A_FAZER = 1
    EM_ANDAMENTO = 2
    CONCLUIDA = 3
