import sys
sys.stdout.reconfigure(encoding='utf-8')
from views.menu import menu_tarefas

if __name__ == "__main__":
    menu_tarefas()
    