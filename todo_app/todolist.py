while True:
    user_action = input(
        "Enter 'add', 'view', 'edit', 'done' to complete a task or 'quit' to quit: ")
    user_action = user_action.strip()

    match  user_action:
        case 'add' | 'a':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'view' | 'show' | 's':
            for index, item in enumerate(todos):
                row = f'{index + 1}. {item.capitalize()}'
                print(row)

            print(f" You have {len(todos)} items on your Todo List")
        case 'edit' | 'e':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo
        case 'complete' | 'done':
            number = int(input("Number of the list to complete?: "))
            todos.pop(number - 1)
        case 'quit' | 'q':
            break

print('Thank You, Good Bye.')
