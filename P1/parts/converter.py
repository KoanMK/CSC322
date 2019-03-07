import non_terminals, terminals
import re

class CNFConverter:
    def __init__(self):
        pass
    
    # outputs the internal CNF tree into input for the minisat (incomplete)
    def clauses(self, tree):
        num_clauses = 1
        # num_vars = 0
        # clauses = []
        if type(tree) is terminals.Terminal:
            return tree.get_var()
        if type(tree) is non_terminals.AndOP:
            num_clauses += 1
            next_left = self.clauses(tree.get_left())
            next_right = self.clauses(tree.get_right())
            return [next_left, next_right]

    # converts the internal tree to CNF
    def cnf(self, tree):
        rtree = self.imps(tree)
        rtree = self.demorgans(rtree)
        rtree = self.distr(rtree)
        return rtree
    
    def imps(self, tree):
        if type(tree) is terminals.Terminal:
            return tree
        elif type(tree) is non_terminals.ImpOP:
            new_or = non_terminals.OrOP()
            new_not = non_terminals.NegOP()
            new_not.set_child(self.imps(tree.get_left()))
            new_or.set_left(new_not)
            new_or.set_right(self.imps(tree.get_right()))
            return new_or
        elif type(tree) is non_terminals.NegOP:
            tree.set_child(self.imps(tree.get_child()))
            return tree
        else:
            tree.set_left(self.imps(tree.get_left()))
            tree.set_right(self.imps(tree.get_right()))
            return tree

    def demorgans(self, tree):
        if type(tree) is terminals.Terminal:
            return tree
        elif type(tree) is non_terminals.NegOP:
            x = tree.get_child()
            if type(x) is non_terminals.NegOP:
                return self.demorgans(x.get_child())
            elif type(x) is non_terminals.AndOP:
                new_or = non_terminals.OrOP()
                new_not_left = non_terminals.NegOP()
                new_not_right = non_terminals.NegOP()

                new_not_left.set_child(x.get_left())
                new_not_right.set_child(x.get_right())

                new_or.set_left(self.demorgans(new_not_left))
                new_or.set_right(self.demorgans(new_not_right))
                return new_or
            elif type(x) is non_terminals.OrOP:
                new_and = non_terminals.AndOP()
                new_not_left = non_terminals.NegOP()
                new_not_right = non_terminals.NegOP()

                new_not_left.set_child(x.get_left())
                new_not_right.set_child(x.get_right())

                new_and.set_left(self.demorgans(new_not_left))
                new_and.set_right(self.demorgans(new_not_right))
                return new_and
            tree.set_child(self.demorgans(x))
            return tree
        else:
            tree.set_left(self.demorgans(tree.get_left()))
            tree.set_right(self.demorgans(tree.get_right()))
            return tree

    def distr(self, tree):
        if type(tree) is terminals.Terminal:
            return tree
        elif type(tree) is non_terminals.OrOP:
            x = tree.get_left()
            if type(x) is non_terminals.AndOP:
                new_and = non_terminals.AndOP()
                new_or_left = non_terminals.OrOP()
                new_or_right = non_terminals.OrOP()

                new_or_left.set_left(x.get_left())
                new_or_left.set_right(tree.get_right())

                new_or_right.set_left(x.get_right())
                new_or_right.set_right(tree.get_right())

                new_and.set_left(new_or_left)
                new_and.set_right(new_or_right)
                return self.distr(new_and)
            y = tree.get_right()
            if type(y) is non_terminals.AndOP:
                new_and = non_terminals.AndOP()
                new_or_left = non_terminals.OrOP()
                new_or_right = non_terminals.OrOP()

                new_or_left.set_left(y.get_left())
                new_or_left.set_right(tree.get_left())

                new_or_right.set_left(y.get_right())
                new_or_right.set_right(tree.get_left())

                new_and.set_left(new_or_left)
                new_and.set_right(new_or_right)
                return self.distr(new_and)
            tree.set_left(self.distr(tree.get_left()))
            tree.set_right(self.distr(tree.get_right()))
            return tree
        elif type(tree) is non_terminals.NegOP:
            tree.set_child(self.distr(tree.get_child()))
            return tree
        else:
            tree.set_left(self.distr(tree.get_left()))
            tree.set_right(self.distr(tree.get_right()))
            return tree
