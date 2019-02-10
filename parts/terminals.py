import expression

class Terminal(expression.Expression):
    def __init__(self, var):
        self.__var = var
    
    def set_var(self, var):
        self.__var = var

    def set_value(self, value):
        self.__value = value

    def get_var(self):
        return str(self.__var)

    def get_value(self):
        return str(self.__value)
 