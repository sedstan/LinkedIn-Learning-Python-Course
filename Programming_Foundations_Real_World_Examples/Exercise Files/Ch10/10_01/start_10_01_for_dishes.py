""" Loading the Dishwasher """

# dirty dishes in the sink
sink = ['bowl','plate','cup']

for dish in list(sink):
    # print('Putting {} in the dishwasher'.format(dish))
    print(f"Putting {dish} in the dishwasher.")
    print(sink.remove(dish))
    print(sink)