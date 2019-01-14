class Borg:
    
    """The Borg design pattern"""
    
    _shared_state = {} # Attribute dictionary
    
    def __init__(self):
        self.__dict__ = self._shared_state # Make it an attribute dictionary

class Singleton(Borg):  # Inherits from the Borg class
    """ now shares all attributes from borg"""

    """The singleton class"""
    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)
    
    def __str__(self):
        # REturns the attribute dictionary for printing
        return str(self._shared_state)
# Let's create a signleton object and add our first acronym
x = Singleton(HTTP = 'Hyper Text Transfer Protocol')
# Print the object
print(x)
# Let's create another singleton object and if it refers to the same attribute dictionary by adding another accronym.
y = Singleton(SNMP = 'Simple Network Protocol')
# Print the object.
print(y)
