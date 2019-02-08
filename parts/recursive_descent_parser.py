import non_terminals, terminals

class RecursiveDescentParser:
    def __init__(self, lexer):
        # transcribe parser code from java example:
        # https://unnikked.ga/how-to-build-a-boolean-expression-evaluator-518e9e068a65
        self.lexer = lexer
        self.root = None
    
    def factor(self):
        pass

    def term(self):
        pass

    def expression(self):
        pass

    def build(self):
        expression()
        return self.root
