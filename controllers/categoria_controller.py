from database.conexao import conectar
from models.categoria import Categoria

#Função para criar categoria
def criar_categoria(nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categoria (nome) VALUES (%s) RETURNING id", (nome,))
    cat_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return Categoria(id=cat_id, nome=nome)

#Função para Listar categorias
def listar_categorias():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM categoria")
    resultados = cursor.fetchall()
    categorias = [Categoria(id=r[0], nome=r[1]) for r in resultados]
    cursor.close()
    conn.close()
    return categorias
