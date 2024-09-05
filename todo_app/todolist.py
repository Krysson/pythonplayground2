todos = []

while True:
  user_action = input("Enter 'add', 'view', 'edit', 'done' to complete a task or 'quit' to quit: ")
  user_action = user_action.strip()

  match  user_action:
      case 'add' | 'a':
        todo = input("Enter a todo: ")
        todos.append(todo)
      case 'view' | 'show':
        for index, todo in enumerate(todos):
            print(f"{index + 1}. {todo.capitalize()}")
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