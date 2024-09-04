todos = []

while True:
  user_action = input("Type 'add' to add a todo, 'view' to view your todos, 'edit' to edit a todo or 'quit' to quit: ")
  user_action = user_action.strip()

  match  user_action:
      case 'add' | 'a':
        todo = input("Enter a todo: ")
        todos.append(todo)
      case 'view' | 'show':
        for todo in todos:
          print(todo)
      case 'edit':
        number = int(input("Number of the todo to edit: "))
        existing_todo = todos[number]
        print(existing_todo)
      case 'quit' | 'q':
        break

print('Thank You, Good Bye.')