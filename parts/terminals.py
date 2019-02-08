import expression

class Terminal(expression.Expression):
    def __init__(self, var, value):
        self.__var = var
        self.__value = value
    
    def var(self):
        return str(self.__var)

    def value(self):
        return str(self.__value)
 