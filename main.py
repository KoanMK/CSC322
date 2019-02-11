from parts import lexer, recursive_descent_parser, converter
import os
import re

if __name__ == '__main__':
    while True:
        input = raw_input("> ")
        if input == "exit":
            break
        
        if input == "vcheck1":
            lexer = lexer.Lexer()
            parser = recursive_descent_parser.RecursiveDescentParser(lexer)

            parser.build()
            print "INITIAL TREE: "
            parser.print_tree(parser.root, 0)

            cnf = converter.CNFConverter()
            x = cnf.cnf(parser.root)

            print "\nCNF TREE: "
            parser.print_tree(x, 0)
        else:
            print "Sorry, that command isn't implemented yet..."
