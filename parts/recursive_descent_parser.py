class RecursiveDescentParser:
    def __init__(self, lexer):
        # transcribe parser code from java example:
        # https://unnikked.ga/how-to-build-a-boolean-expression-evaluator-518e9e068a65
        self.lexer = lexer
        self.symbol = None
