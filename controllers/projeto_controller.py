from database.conexao import conectar
from models.projeto import Projeto

# Função para criar um projeto
def criar_projeto(nome, descricao=""):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projeto (nome, descricao) VALUES (%s, %s) RETURNING id", (nome, descricao))
    projeto_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return Projeto(projeto_id, nome, descricao)

# Lista todos os projetos
def listar_projetos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, descricao FROM projeto")
    resultados = cursor.fetchall()
    conn.close()
    return [Projeto(id=r[0], nome=r[1], descricao=r[2]) for r in resultados]
