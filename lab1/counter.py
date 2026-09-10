"""
File: counter.py
Defines a Counter class for counting.
"""

class Counter(object):
    """Models a counter."""
    
   #Constructor
    def __init__(self):                           # Usage: c = Counter() 
        """Sets up the counter."""
        self.reset()
        
    # Mutator methods
    def reset(self):                              # Usage: c.reset()  
        """Sets the counter to 0."""
        self.value = 0
        
    def increment(self, amount = 1):              # Usage: c.increment()      
        """Adds amount to the counter."""
        self.value += amount
        

    def decrement(self, amount = 1):              # Usage: c.decrement()
        """Subtracts amount from the counter."""
        self.value -= amount
        

    # Accessor methods
    def getValue(self):                          # Usage: v = c.getValue()
        """Returns the counter's value."""
        return self.value
    

    def __str__(self):                           # Usage: str(c), print(c)
        """Returns the string representation of the counter."""
        return str(self.value)
    
    def __eq__(self, other):                     # Usage: c1 == c2, c1 != c2
        """Returns True if self equals other
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other): return False
        return self.value == other.value

def main():
    """A short tester function to exercise the Counter
    methods."""
    c = Counter()
    print("Value at startup:", c)
    print("Values after 5 increments:")
    for x in range(5):
        c.increment()
        print(c.getValue(), end = " ")
    print("\nValues after 7 decrements:")
    for x in range(7):
        c.decrement()
        print(c.getValue(), end = " ")
    c.reset()
    print("\nValue after reset:", c)
    c2 = Counter()
    print("Value of c:", c, ", value of c2:", c2)
    print("Expect True for c is c:", c is c)
    print("Expect False for c is c2:", c is c2)
    print("Expect True for c == c2:", c == c2)
    c2.increment()
    print("c2 incremented, expect False for c == c2:", c == c2)
         

# Entry point of the application.
if __name__ == "__main__":
    main()

