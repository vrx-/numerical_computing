# Backpack.py
""" Volume II Lab 2: Object Oriented Programming (Auxiliary file)
    Modify this file for problems 1 and 3.
    <Name>
    <Class>
    <Date>
"""

# Problem 1: Modify this class. Add 'name' and max_size' attributes, modify
#   the put() method, and add a dump() method. Remember to update docstrings.
class Backpack:
    """Backpack object. Has a color and a list of contents.
    
    Attributes:
        color (str): the color of the backpack.
        contents (list): the contents of the backpack.
        # ADD ATTRIBUTE INFO HERE AS YOU EXPAND THIS CLASS
        # Good docstrings are required for full credit.
    """
    
    def __init__(self, color = 'black'):
        """Constructor for a backpack object. Set the color and initialize the
        contents list.
        
        Inputs:
            color (str, opt): the color of the backpack. Defaults to 'black'.
            # ADD INPUTS INFO HERE AS YOU EXPAND THIS FUNCTION
        
        Returns:
            A backpack object wth no contents.
        """
        
        self.color = color
        self.contents = []
    
    def put(self, item):
        """Add 'item' to the backpack's content list."""
        self.contents.append(item)
    
    def take(self, item):
        """Remove 'item' from the backpack's content list."""
        self.contents.remove(item)
    
    # -------------------- Magic Methods (Problem 3) -------------------- #
    
    def __add__(self, other):
        """Add the contents of 'other' to the contents of 'self'.
        Note that the contents of 'other' are unchanged.
        
        Inputs:
            self (Backpack): the backpack on the left-hand side of the
                addition operator.
            other (Backpack): The backpack on the right-hand side of the
                addition operator.
        """
        self.contents = self.contents + other.contents
    
    def __lt__(self, other):
        """Compare two backpacks. If 'self' has fewer contents than 'other',
        return True. Otherwise, return False.
        
        Inputs:
            self (Backpack): the backpack on the left-hand side of the
                inequality.
            other (Backpack): The backpack on the right-hand side of the
                inequality.
        """
        
        if len(self.contents) < len(other.contents):
            return True
        else:
            return False
    
    # Problem 3: write the __str__ and __eq__ magic methods for the Backpack.
    def __str__(self):
        """String Representation.
        Examples:
            >>> b = Backpack()             |    Or,
            >>> b.put('something')         |
            >>> b.put('something else')    |    >>> c = Backpack('red','Bob',3)
            >>> print(b)                   |    >>> print(c)
            Name:       backpack           |    Name:       Bob
            Color:      black              |    Color:      red
            Size:       2                  |    Size:       0
            Max Size:   5                  |    Max Size:   3
            Contents:                      |    Contents:   Empty
                        something          |
                        something else     |
        """
        pass
    
    def __eq__(self,other):
        """WRITE A SHORT DOCSTRING HERE"""
        pass

# ============================== END OF FILE ============================== #
