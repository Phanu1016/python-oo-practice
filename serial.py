"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """ Constructor for SerialGenerator """
        self.start = self.current = start - 1
    
    def generate(self):
        """ Generate a number base on the start value """
        self.current += 1
        return self.current

    def reset(self):
        """ Reset the current value to starting value """
        self.current = self.start

    