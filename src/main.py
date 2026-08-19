import json

def load_tasks():
    try: 
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def show_tasks():
    if len(tasks) == 0:
        print("\nAinda não existem tarefas!\n")
        return
    for index, task in enumerate(tasks):
        print(index + 1, task["description"])

        if task["completed"]:
            print ("Concluída")
        else:
            print ("Pendente")

def add_task():
    task_description=input ("\nDigite uma nova tarefa: ")
    task_description = task_description.strip()
    if len(task_description) == 0:
        print("\nA tarefa não pode estar vazia!\n")
    else:
        tasks.append({"description" : task_description,
        "completed" : False})
        save_tasks()

def complete_task():
    show_tasks()
    try:
        task_number = int(input("\nDigite o número da task que deseja marcar como Concluída: "))
        task_index = task_number - 1
    except ValueError:
        print("\nVocê precisa digitar um número!\n")
        return
    if 0 <= task_index < len(tasks):
        if tasks[task_index]["completed"]:
            print ("\nEssa tarefa já foi concluída!\n")
        else:
            tasks[task_index]["completed"] = True
            show_tasks()
            save_tasks()
    else:
        print("\nNúmero inválido!\n")

def delete_task():
    if len(tasks) == 0:
        print("\nNão há tarefas para excluir!\n")
        return
    show_tasks()
    try:
        task_number = int(input("\nDigite o número da task que deseja excluir: "))
        task_index = task_number - 1
    except ValueError:
        print("\nVocê precisa digitar um número!\n")
        return
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks()
        print("\nTarefa excluída com sucesso!\n")
    else:
        print("\nNúmero inválido!\n")

tasks = load_tasks()

running  = True

while running:

    choice = input("\n1 - Adicionar tarefa\n2 - Ver tarefas\n3 - Concluir tarefa\n4 - Excluir tarefa\n5 - Sair\n")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        running = False
    else:
        print("\nOpção inválida!\n")
