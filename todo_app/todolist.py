# ToDo List App

while True:
    # Prompt the user for an action and strip any leading/trailing whitespace
    user_action = input(
        "Enter 'add', 'view', 'edit', 'done' to complete a task or 'quit' to quit: ")
    user_action = user_action.strip()

    # Match the user action to the corresponding case
    match user_action:

        case 'add' | 'a':
            # Add a new todo item
            todo = input("Enter a todo: ") + "\n"

            with open('todo_app/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todo_app/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'view' | 'show' | 's':
            # View all todo items
            with open('todo_app/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index + 1}. {item.capitalize()}'
                print(row)

            print(f" You have {len(todos)} items on your Todo List")

        case 'edit' | 'e':
            # Edit an existing todo item
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open('todo_app/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + '\n'

            with open('todo_app/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete' | 'done':
            # Mark a todo item as complete (remove it from the list)
            number = int(input("Number of the list to complete?: "))

            with open('todo_app/todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todo_app/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Task {todo_to_remove.capitalize()} has been removed."
            print(message)

        case 'quit' | 'q':
            # Exit the loop and end the program
            break

print('Thank You, Good Bye.')

# start LIST COMPREHENSION strips the \n new line from the list so there are not line breaks
# should be added to the view case
# new_todos = [item.strip('\n') for item in todos]
# end
