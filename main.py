from parts import lexer, recursive_descent_parser
import os
import re

if __name__ == '__main__':
    # get user input
    var = raw_input("Enter expression: ")
    print var
    # parse input
    # x = lexer.Lexer()
    # print x.EOF