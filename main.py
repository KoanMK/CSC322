from parts import lexer, recursive_descent_parser
import os
import re

if __name__ == '__main__':
    # get user input
    # input = raw_input("Enter expression: ")
    # parse input
    lexer = lexer.Lexer()
    parser = recursive_descent_parser.RecursiveDescentParser(lexer)

    parser.build()