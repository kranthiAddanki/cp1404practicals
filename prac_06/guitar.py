CURRENT_YEAR = 2024
VINTAGE_AGE = 50


class Guitar:
    """ Guitar class with attributes and methods"""

    def __init__(self, name="", year=0, cost=0):
        """ Initaliase a guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """ Return the current age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Check if the guitar is in a vintage based on condition"""
        if self.get_age() >= VINTAGE_AGE:
            return "TRUE"
        else:
            return "FALSE"


