# Least to Greatest
pointsInAGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointsInAGame)
print(sortedGame)
# Alphabetically
children = ['Sue', 'Jerry', 'Linda']
print(sorted(children))
print(sorted(['Sue', 'jerry', 'linda']))
# Key Parameters
print(sorted("My favourite child is Linda".split(), key=str.upper))
print(sorted(pointsInAGame, reverse=True))

leaderBoard = {231:'ckl', 123:'abc', 432:'jkc'}
print(sorted(leaderBoard, reverse=True))
print(leaderBoard.get(432))

students = [('alice', 'b',12), ('eliza', 'a', 16, ('tae', 'c', 15))]
print(sorted(students, key=lambda student: student[0]))
print(sorted(students, key=lambda student: student[1]))
print(sorted(students, key=lambda student: student[2]))