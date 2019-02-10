import non_terminals, terminals
import re

class RecursiveDescentParser:
    def __init__(self, lexer):
        # transcribe parser code from java example:
        # https://unnikked.ga/how-to-build-a-boolean-expression-evaluator-518e9e068a65
        self.lexer = lexer
        self.root = None
        self.symbol = None
    
    # ATOM ::= VAR | LPAREN SENT RPAREN
    def atom(self):
        self.symbol = self.lexer.next_symbol()
        try:
            var = re.findall("^A[1-9][0-9]*$", self.symbol)
            # print "ATOM IS: " + self.symbol
        except TypeError:
            var = None
            print "Regex messed up for some reason..."

        if var:
            # terminal = terminals.Terminal(self.symbol)
            # self.root = terminal
            self.root = self.symbol
            self.symbol = self.lexer.next_symbol()
            # print "ATOM: ROOT IS " + self.root.get_var()
            print "ATOM: ROOT IS " + self.root
        elif self.symbol is self.lexer.NEGOP:
            neg = non_terminals.NegOP()
            self.atom()
            neg.set_child(self.root)
            self.root = neg
            print "NEG: CHILD IS: " + str(self.root.get_child())
        elif self.symbol is self.lexer.LPAREN:
            # print "LPAREN1: ROOT IS " + self.symbol
            self.sent()
            self.symbol = self.lexer.next_symbol()
        else:
            raise ValueError('Expression Malformed')

    # LIT ::= ATOM | NEGOP ATOM
    def lit(self):
        self.atom()
        if self.symbol is self.lexer.NEGOP:
            neg = non_terminals.NegOP()
            self.atom()
            neg.set_child(self.root)
            self.root = neg
            print "NEG: CHILD IS: " + str(self.root.get_child())
    
    # CONJ ::= LIT{ANDOP LIT}
    def conj(self):
        self.lit()
        if self.symbol is self.lexer.ANDOP:
            andop = non_terminals.AndOP()
            andop.set_left(self.root)
            self.lit()
            andop.set_right(self.root)
            self.root = andop
            print "CONJ - LEFT: " + str(self.root.get_left()) + ", RIGHT: " + str(self.root.get_right())

    # DISJ ::= CONJ{OROP CONJ}
    def disj(self):
        self.conj()
        if self.symbol is self.lexer.OROP:
            orop = non_terminals.OrOP()
            orop.set_left(self.root)
            self.conj()
            orop.set_right(self.root)
            self.root = orop
            print "DISJ - LEFT: " + str(self.root.get_left()) + ", RIGHT: " + str(self.root.get_right())

    # SENT ::= DISJ | DISJ IMPOP SENT
    def sent(self):
        self.disj()
        if self.symbol is self.lexer.IMPOP:
            impop = non_terminals.ImpOP()
            impop.set_left(self.root)
            self.sent()
            impop.set_right(self.root)
            self.root = impop
            print "IMPOP - LEFT: " + str(self.root.get_left()) + ", RIGHT: " + str(self.root.get_right())

    def build(self):
        self.sent()
        return self.root
