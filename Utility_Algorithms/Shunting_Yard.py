def shunting_yard(expression):

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}
    output_queue = []
    operator_stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isnumeric():  
            output_queue.append(token)
        elif token in precedence:
            while (operator_stack and
                   operator_stack[-1] != '(' and
                   (precedence[operator_stack[-1]] > precedence[token] or
                    (precedence[operator_stack[-1]] == precedence[token] and associativity[token] == 'L'))):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':  
            operator_stack.append(token)
        elif token == ')':  
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop() 
    
    while operator_stack:
        output_queue.append(operator_stack.pop())
    
    return ' '.join(output_queue)


#test
expression = "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"
result = shunting_yard(expression)
print("Postfix notation:", result)
