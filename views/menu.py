from datetime import datetime
from controllers.usuario_controller import criar_usuario, listar_usuarios
from controllers.projeto_controller import criar_projeto, listar_projetos
from controllers.categoria_controller import criar_categoria, listar_categorias
from controllers.tarefa_controller import criar_tarefa, listar_tarefas
from models.enums import Prioridade, Status

#Função do Menu
def menu_tarefas():
    """
    Menu interativo para criação e listagem de Usuários, Projetos, Categorias e Tarefas.
    """
    while True:
        print("\n--- MENU DE TAREFAS ---")
        print("1 - Criar Usuário")
        print("2 - Listar Usuários")
        print("3 - Criar Projeto")
        print("4 - Listar Projetos")
        print("5 - Criar Categoria")
        print("6 - Listar Categorias")
        print("7 - Criar Tarefa")
        print("8 - Listar Tarefas")
        print("0 - Sair")
        opcao = input("Escolha: ")

        # --- Usuário ---
        if opcao == "1":
            nome = input("Nome do usuário: ")
            email = input("Email do usuário: ")
            usuario = criar_usuario(nome, email)
            print(f"Usuário criado: {usuario}")

        elif opcao == "2":
            usuarios = listar_usuarios()
            if not usuarios:
                print("Nenhum usuário encontrado.")
            for u in usuarios:
                print(u)

        # --- Projeto ---
        elif opcao == "3":
            nome = input("Nome do projeto: ")
            descricao = input("Descrição do projeto: ")
            projeto = criar_projeto(nome, descricao)
            print(f"Projeto criado: {projeto}")

        elif opcao == "4":
            projetos = listar_projetos()
            if not projetos:
                print("Nenhum projeto encontrado.")
            for p in projetos:
                print(p)

        # --- Categoria ---
        elif opcao == "5":
            nome = input("Nome da categoria: ")
            categoria = criar_categoria(nome)
            print(f"Categoria criada: {categoria}")

        elif opcao == "6":
            categorias = listar_categorias()
            if not categorias:
                print("Nenhuma categoria encontrada.")
            for c in categorias:
                print(c)

        # --- Tarefa ---
        elif opcao == "7":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            projeto_id = int(input("ID do projeto: "))
            responsavel_id = int(input("ID do responsável: "))
            categoria_id = int(input("ID da categoria: "))

            # Captura as opções e converte para Enum
            prioridade_input = int(input("Prioridade (1=BAIXA, 2=MEDIA, 3=ALTA): "))
            status_input = int(input("Status (1=A_FAZER, 2=EM_ANDAMENTO, 3=CONCLUIDA): "))

            prioridade = Prioridade(prioridade_input)
            status = Status(status_input)

            while True:
                prazo_input = input("Prazo (dd/mm/yyyy): ")
                try:
                    prazo = datetime.strptime(prazo_input, "%d/%m/%Y").date()
                    if prazo < datetime.today().date():
                        print("Erro: O prazo não pode ser menor que a data de hoje.")
                    else:
                        break
                except ValueError:
                    print("Formato de data inválido. Use dd/mm/yyyy.")

            criar_tarefa(titulo, descricao, projeto_id, responsavel_id, categoria_id,
                         prioridade, status, prazo)

        elif opcao == "8":
            listar_tarefas()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
