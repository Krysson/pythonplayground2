from operator import index

ranking = ['John', 'Sen', 'Lisa']

name = input('Enter a Name: ')

rank = ranking.index(name)
rank = rank + 1
print(rank)

# while   True :
#     match name:
#         case 'John' | 'john':
#             print(ranking[0])
#             break
#         case 'sen' | 'Sen':
#
#             print(ranking[1])
#             break
#         case 'List' | 'lisa':
#
#             print(ranking[2])
#             break
#         case 'q':
#             break
