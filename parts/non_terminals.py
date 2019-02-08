import expression

class NonTerminal(expression.Expression):
    def __init__(self):
        pass
    
    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right

class OrOP(NonTerminal):
    def __init__(self):
        pass

class AndOP(NonTerminal):
    def __init__(self):
        pass

class ImpOP(NonTerminal):
    def __init__(self):
        pass

class NegOP(NonTerminal):
    def set_child(self, child):
        self.child = child

class LParen(NonTerminal):
    def __init__(self):
        pass

class RParen(NonTerminal):
    def __init__(self):
        pass

