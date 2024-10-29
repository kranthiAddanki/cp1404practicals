# Expected time 15 minutes, Actual time 60 minutes
class ProgrammingLanguage:
    """Represents information about programming languages."""


    def __init__(self, field, typing, reflection, year):
        """Construct a programming language using given values."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year


    def is_dynamic(self):
        """Check if the language is dynamically typed."""
        return self.typing == "Dynamic"


    def __str__(self):
        """Return string representation """
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
