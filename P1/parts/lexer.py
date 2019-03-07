import re
import tokenizer

class Lexer:
    def __init__(self):
        self.symbol = None
        self.INVALID = "-1"
        self.NONE = "0"
        self.OROP = "1"
        self.ANDOP = "2"
        self.NEGOP = "3"
        self.IMPOP = "4"
        self.LPAREN = "5"
        self.RPAREN = "6"
        self.switcher = {
            "INVALID": self.INVALID,
            "v": self.OROP,
            "&": self.ANDOP,
            "~": self.NEGOP,
            "->": self.IMPOP,
            "(": self.LPAREN,
            ")": self.RPAREN,
        }
        # get input from user
        self.input = raw_input("Enter expression: ")
        # create stream from input
        self.stream = tokenizer.Tokenizer(self.input)
    
    # get next symbol and return it
    def next_symbol(self):
        try:
            next = self.stream.next_token()
            self.symbol = self.switcher.get(next, next)
            return self.symbol
        except IOError:
            print "An error occured when accessing next token."
