names_list = ['Adam','Anne','Barry','Brianne','Charlie','Cassandra','David','Dana']

print(names_list)
#Converts names to uppercase
uppercase_names = (name.upper() for name in names_list)
print(list(uppercase_names))