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
          print(todo.capitalize())
      case 'edit' | 'e':
        number = int(input("Number of the todo to edit: "))
        number = number - 1
        new_todo = input("Enter the new todo: ")
        todos[number] = new_todo        
      case 'quit' | 'q':
        break

print('Thank You, Good Bye.')