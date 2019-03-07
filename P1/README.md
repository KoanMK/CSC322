# CSC 322
## Assignment 1
  
Nigel Decontie (V00853112)

## Overview
These are the project files for Assignment 1 of CSC322.
The project is incomplete as the group suffered casualties (they dropped) and I am the sole survivor.   
From Task 1: The files read in an expression, convert it to tokens, create an internal tree representation and convert the tree to CNF.
Tasks 2, 3 and 4 were not completed.

## Usage
Run command:  
> $python main.py

## Commands
> vcheck1
- Allows you to input an expression to be translated into a CNF tree.
- The expression should have no whitespace and follow the outline for permitted characters as in the 322proj1.pdf.

> exit
- Exits the program.

## Files
#### main.py
Launches the files. Uncomment lines 
#### lexer.py
Creates a tokenizer and classifies the input characters.
#### tokenizer.py
Creates a stream from the input expression.
#### recursive_descent_parser.py
Uses the token stream to create an internal tree representation of the expression.
#### converter.py
Converts the tree into CNF form.
