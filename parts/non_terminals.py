import expression

class NonTerminal(expression.Expression):
    def __init__(self):
        pass
    
    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right
    
    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

class OrOP(NonTerminal):
    def __str__(self):
        return "OROP"

class AndOP(NonTerminal):
    def __str__(self):
        return "ANDOP"

class ImpOP(NonTerminal):
    def __str__(self):
        return "IMPOP"

class NegOP(NonTerminal):
    def set_child(self, child):
        self.child = child

    def get_child(self):
        return self.child
    
    def __str__(self):
        return "NEGOP"

class LParen(NonTerminal):
    def __str__(self):
        return "LPAREN"

class RParen(NonTerminal):
    def __str__(self):
        return "RPAREN"

