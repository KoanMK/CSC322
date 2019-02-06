import re

class Lexer:
    def __init__(self, input):
        self.input = input
        self.symbol = None
        self.EOL = -3
        self.EOF = -2
        self.INVALID = -1
        self.NONE = 0
        self.OR = 1
        self.AND = 2
        self.NOT = 3
        self.TRUE = 4
        self.FALSE = 5
        self.LEFT = 6
        self.RIGHT = 7
        self.TRUE_LITERAL = "true"
        self.FALSE_LITERAL = "false"
    
    def next_symbol(self):
        tokens = re.compile("(A[1-9][0-9]*)|(&)|(v)|(~)|(\()|(\))")
        # create token stream from input and implement lexer code from java example:
        # https://unnikked.ga/how-to-build-a-boolean-expression-evaluator-518e9e068a65
        