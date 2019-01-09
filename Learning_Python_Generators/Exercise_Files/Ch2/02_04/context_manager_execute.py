from context_manager_as import new_log_file

with new_log_file('logfile') as file:
    file.write('this is the body')