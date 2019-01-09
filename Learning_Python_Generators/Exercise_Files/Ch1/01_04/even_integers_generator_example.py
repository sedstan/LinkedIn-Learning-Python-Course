from even_integers_generator import even_integers_generator

integers = even_integers_generator(10)
# print(integers.__next__())
# print(integers.__next__())
# print(integers.__next__())
# print(integers.__next__())
# print(integers.__next__())
# print(integers.__next__())

# for n in integers:
#     print(n)

# print(integers.__next__())

# integers = even_integers_generator(10)
# for n in integers:
#     print(n)

# for n in even_integers_generator(10):
#     print(n)

# for n in (i for i in range(10)):
#     print(n)

# print(max(i for i in range(10)))

# can't be reused
# Calling next()  on an exhausted generator raises stopiteration
# for loop handles stopiteration

# can be passed to a function
