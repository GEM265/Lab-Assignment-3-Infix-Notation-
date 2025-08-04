# Lab-Assignment-3-Infix-Notation-
Write a Python program that asks the user to enter a mathematical expression in Infix notation 

e.g :  3 + 5 * ( 2 - 8 )   and then:

 
1. Convert it into Postfix notation (Reverse Polish Notation) (25 points)

def infix_to_postfix(infix : string) : returns postfix:string

 

2. Convert it into Prefix notation (Polish Notation) (25 points)

def infix_to_prefix(infix: string) : returns prefix:string

 

3. Evaluate the expression using Postfix evaluation (25 points)

def evaluate_postfix(postfix: string)  :  returns result

 

4. Evaluate the expression using Prefix evaluation (25 points)

def evaluate_prefix(prefix:string)  : returns result

 

Requirements

- Implement the functions: infix_to_postfix, infix_to_prefix, evaluate_postfix, evaluate_prefix
The program should support operators: +, -, *.
The program should correctly handle parentheses for operator precedence.
Use only single digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9).

Simple output :


image.png

