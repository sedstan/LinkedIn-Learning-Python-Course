from coroutine_example import coroutine_example

c = coroutine_example()
c.__next__()
c.send(10)
