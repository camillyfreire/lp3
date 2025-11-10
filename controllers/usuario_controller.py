from database.conexao import conectar
from models.usuario import Usuario

# Função para criar um novo usuário
def criar_usuario(nome, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuario (nome, email) VALUES (%s, %s) RETURNING id", (nome, email))
    usuario_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return Usuario(id=usuario_id, nome=nome, email=email)

# Listar todos os usuários
def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM usuario")
    resultados = cursor.fetchall()
    conn.close()
    return [Usuario(id=r[0], nome=r[1], email=r[2]) for r in resultados]
