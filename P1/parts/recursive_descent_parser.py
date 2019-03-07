import non_terminals, terminals
import re

class RecursiveDescentParser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.root = None
        self.symbol = None
    
    # ATOM ::= VAR | LPAREN SENT RPAREN
    def atom(self):
        self.symbol = self.lexer.next_symbol()
        try:
            var = re.findall("^A[1-9][0-9]*$", self.symbol)
        except TypeError:
            var = None

        if var:
            terminal = terminals.Terminal(self.symbol)
            self.root = terminal
            self.symbol = self.lexer.next_symbol()

        elif self.symbol is self.lexer.NEGOP:
            neg = non_terminals.NegOP()
            self.atom()
            neg.set_child(self.root)
            self.root = neg

        elif self.symbol is self.lexer.LPAREN:
            self.sent()
            self.symbol = self.lexer.next_symbol()
        else:
            raise ValueError('Malformed Expression')

    # LIT ::= ATOM | NEGOP ATOM
    def lit(self):
        self.atom()
        if self.symbol is self.lexer.NEGOP:
            neg = non_terminals.NegOP()
            self.atom()
            neg.set_child(self.root)
            self.root = neg
    
    # CONJ ::= LIT{ANDOP LIT}
    def conj(self):
        self.lit()
        if self.symbol is self.lexer.ANDOP:
            andop = non_terminals.AndOP()
            andop.set_left(self.root)
            self.lit()
            andop.set_right(self.root)
            self.root = andop

    # DISJ ::= CONJ{OROP CONJ}
    def disj(self):
        self.conj()
        if self.symbol is self.lexer.OROP:
            orop = non_terminals.OrOP()
            orop.set_left(self.root)
            self.conj()
            orop.set_right(self.root)
            self.root = orop

    # SENT ::= DISJ | DISJ IMPOP SENT
    def sent(self):
        self.disj()
        if self.symbol is self.lexer.IMPOP:
            impop = non_terminals.ImpOP()
            impop.set_left(self.root)
            self.sent()
            impop.set_right(self.root)
            self.root = impop

    def build(self):
        self.sent()
        return self.root

    # prints the tree to console
    def print_tree(self, tree, level):
        print str(level) + ". " + str(tree)
        try:
            self.print_tree(tree.get_left(), level+1)
        except AttributeError:
            pass
        try:
            self.print_tree(tree.get_right(), level+1)
        except AttributeError:
            pass
        try:
            self.print_tree(tree.get_child(), level+1)
        except AttributeError:
            pass
