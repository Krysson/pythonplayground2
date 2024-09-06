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

            file = open('todo_app/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todo_app/todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'view' | 'show' | 's':
            # View all todo items
            file = open('todo_app/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index + 1}. {item.capitalize()}'
                print(row)

            print(f" You have {len(todos)} items on your Todo List")

        case 'edit' | 'e':
            # Edit an existing todo item
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo

        case 'complete' | 'done':
            # Mark a todo item as complete (remove it from the list)
            number = int(input("Number of the list to complete?: "))
            todos.pop(number - 1)

        case 'quit' | 'q':
            # Exit the loop and end the program
            break

print('Thank You, Good Bye.')

# start LIST COMPREHENSION strips the \n new line from the list so there are not line breaks
# should be added to the view case
# new_todos = [item.strip('\n') for item in todos]
# end
