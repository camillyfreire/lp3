#importar 
import psycopg2


#Função para conectar no postgreSQL
def conectar():
    return psycopg2.connect(
        host="localhost",
        database="Projeto_Tarefas",
        user="postgres",
        password="teste"
    )
