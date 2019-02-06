class Lexer:
    def __init__(self):
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