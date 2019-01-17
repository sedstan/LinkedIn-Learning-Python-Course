""" Adding and Removing Friends from Sets """

# revised set of friends to invite
invite = set(['Nestor', 'Amanda', 'Olivia'])

print('Verne' in invite)    # False
invite.add('Verne')
print('Verne' in invite)    # True
print(invite)               # set(['Olivia', 'Nestor', 'Amanda', 'Verne'])
invite.add('Olivia')
print(invite)               # set(['Olivia', 'Nestor', 'Amanda', 'Verne'])
invite.remove('Nestor')      
print(invite)               # set(['Olivia', 'Amanda', 'Verne'])
# invite.remove('Nestor')
# print(invite)               # error
print(invite.pop())
print(invite.pop())
print(invite.pop())
print(invite)
