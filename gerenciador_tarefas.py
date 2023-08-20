import json

def show_tasks(tasks):
    if tasks:
        print("Tarefas:")
        for idx, task in enumerate(tasks, start=1):
            status = "Concluída" if task['done'] else "Pendente"
            print(f"{idx}. [{status}] {task['description']}")
    else:
        print("Nenhuma tarefa pendente.")

def add_task(tasks, description):
    tasks.append({'description': description, 'done': False})

def mark_task_done(tasks, task_index):
    if 0 < task_index <= len(tasks):
        tasks[task_index - 1]['done'] = True
        print("Tarefa marcada como concluída.")
    else:
        print("Índice de tarefa inválido.")

def remove_task(tasks, task_index):
    if 0 < task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Tarefa '{removed_task['description']}' removida.")
    else:
        print("Índice de tarefa inválido.")

def main():
    tasks = []

    while True:
        print("\nSelecione a ação:")
        print("1. Mostrar Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")

        choice = input("Digite a opção: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            description = input("Digite a descrição da tarefa: ")
            add_task(tasks, description)
        elif choice == '3':
            show_tasks(tasks)
            task_index = int(input("Digite o número da tarefa para marcar como concluída: "))
            mark_task_done(tasks, task_index)
        elif choice == '4':
            show_tasks(tasks)
            task_index = int(input("Digite o número da tarefa para remover: "))
            remove_task(tasks, task_index)
        elif choice == '5':
            with open("tasks.json", "w") as file:
                json.dump(tasks, file)
            print("Tarefas salvas. Adeus!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
