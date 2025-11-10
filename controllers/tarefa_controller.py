from database.conexao import conectar
from models.tarefa import Tarefa
from models.enums import Prioridade, Status
from datetime import datetime

#Função para criar uma tarefa
def criar_tarefa(titulo, descricao, projeto_id, responsavel_id, categoria_id,
                 prioridade, status, prazo):
    conn = conectar()
    cursor = conn.cursor()

   # Validação do prazo
    if isinstance(prazo, str):
        try:
            prazo = datetime.strptime(prazo, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Formato de data inválido. Use dd/mm/yyyy.")

    if prazo < datetime.today().date():
        raise ValueError("O prazo não pode ser menor que a data de hoje.")

    data_criacao = datetime.now().date()

    cursor.execute("""
        INSERT INTO tarefa (titulo, descricao, projeto_id, responsavel_id, categoria_id, prioridade, status, data_criacao, prazo)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    """, (titulo, descricao, projeto_id, responsavel_id, categoria_id,
          prioridade.name, status.name, data_criacao, prazo))
    
    tarefa_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()

    print(f"Tarefa criada com sucesso! ID: {tarefa_id}")


#Função para Listar as tarefas do banco de dados 
def listar_tarefas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, status, prioridade, prazo FROM tarefa")
    tarefas = cursor.fetchall()
    conn.close()

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    
    for t in tarefas:
        print(f"ID: {t[0]} | {t[1]} | Status: {t[2]} | Prioridade: {t[3]} | Prazo: {t[4]}")
