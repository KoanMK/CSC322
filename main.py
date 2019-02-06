from parts import lexer, recursive_descent_parser
import os
import re

if __name__ == '__main__':
    # get user input
    input = raw_input("Enter expression: ")
    # parse input
    x = lexer.Lexer(input)
    print x.input