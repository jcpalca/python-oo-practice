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

    def __init__(self, start=100):
        """Create serial generator with a default start of 100"""
        self.current = self.original = start

    def __repr__(self):
        """Represents the current instance"""
        return f"<Serial Generator start={self.current}>"

    def generate(self):
        """Increments instance's start value by 1"""
        temp = self.current
        self.current += 1
        return temp

    def reset(self):
        """Resets instance's start value to its original value"""
        self.current = self.original
