""" Overloading a Circuit Breaker """

class CircuitBreaker: 
    
    def __init__(self, max_amps):
        self.capacity = max_amps # max capacity in amps
        self.load = 0            # present load in amps

    def connect(self, amps):
        if self.load + amps > self.capacity:
            raise Exception('connection will exceed capacity')
        elif self.load + amps < 0:
            raise Exception('connection will cause a negative load')
        else: 
            self.load += amps

# create a 20A circuit breaker
cb = CircuitBreaker(20)
print(cb.load)

cb.connect(12)
cb.connect(7)
cb.connect(10)
print(cb.load)