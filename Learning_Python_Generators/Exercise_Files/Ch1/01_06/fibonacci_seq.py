# EAch number in the sequence is the sum of the previous two.
# previous, next, last

from fibonacci_sequence import fibonacci_gen	

fib = fibonacci_gen()

fib.__next__()
print(fib.__next__())

for _ in range(10):
    print(fib.__next__())