# try out the Python queue functions
from collections import deque #optimised for removing items in the queue form both ends.


# TODO: create a new empty deque object that will function as a queue
queue = deque()

# TODO: add some items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)


# TODO: print the queue contents
print(queue)

# TODO: pop an item off the front of the queue
x = queue.popleft() #front of the queue
print(x)
print(queue)