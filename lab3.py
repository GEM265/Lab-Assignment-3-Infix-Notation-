def infix_to_postfix(infix: str) -> str:
    """Convert infix expression to postfix notation"""
    # Define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2}
    
    # Stack for operators and result list
    stack = []
    postfix = []
    
    # Process each character in the infix expression
    for char in infix:
        if char == ' ':
            continue
        elif char.isdigit():
            # If it's a digit, add to result
            postfix.append(char)
        elif char == '(':
            # Push opening parenthesis to stack
            stack.append(char)
        elif char == ')':
            # Pop operators until opening parenthesis
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove the opening parenthesis
        elif char in precedence:
            # Pop operators with higher or equal precedence
            while (stack and stack[-1] != '(' and 
                   stack[-1] in precedence and 
                   precedence[stack[-1]] >= precedence[char]):
                postfix.append(stack.pop())
            stack.append(char)
    
    # Pop remaining operators from stack
    while stack:
        postfix.append(stack.pop())
    
    return ' '.join(postfix)


def infix_to_prefix(infix: str) -> str:
    """Convert infix expression to prefix notation"""
    # Reverse the infix expression
    reversed_infix = infix[::-1]
    
    # Replace '(' with ')' and vice versa
    temp = []
    for char in reversed_infix:
        if char == '(':
            temp.append(')')
        elif char == ')':
            temp.append('(')
        else:
            temp.append(char)
    
    modified_infix = ''.join(temp)
    
    # Get postfix of modified expression
    postfix = infix_to_postfix(modified_infix)
    
    # Reverse the postfix to get prefix
    prefix = postfix[::-1]
    
    return prefix


def evaluate_postfix(postfix: str) -> float:
    """Evaluate postfix expression"""
    stack = []
    tokens = postfix.split()
    
    for token in tokens:
        if token.isdigit():
            # If it's a number, push to stack
            stack.append(int(token))
        else:
            # If it's an operator, pop two operands and apply operation
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            
            stack.append(result)
    
    return float(stack[0])


def evaluate_prefix(prefix: str) -> float:
    """Evaluate prefix expression"""
    stack = []
    tokens = prefix.split()
    
    # Process tokens from right to left
    for token in reversed(tokens):
        if token.isdigit():
            # If it's a number, push to stack
            stack.append(int(token))
        else:
            # If it's an operator, pop two operands and apply operation
            operand1 = stack.pop()
            operand2 = stack.pop()
            
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            
            stack.append(result)
    
    return float(stack[0])


def main():
    """Main function to run the expression converter and evaluator"""
    print("Mathematical Expression Converter and Evaluator")
    print("=" * 50)
    
    # Get input from user
    infix = input("Enter infix expression: ").strip()
    
    # Convert to postfix and prefix
    postfix = infix_to_postfix(infix)
    prefix = infix_to_prefix(infix)
    
    # Evaluate both expressions
    postfix_result = evaluate_postfix(postfix)
    prefix_result = evaluate_prefix(prefix)
    
    # Display results
    print(f"Postfix: {postfix}")
    print(f"Prefix: {prefix}")
    print(f"Postfix Evaluation: {postfix_result}")
    print(f"Prefix Evaluation: {prefix_result}")


if __name__ == "__main__":
    main()