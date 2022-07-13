def are_parentheses_balanced(expression):

    stack = []
    matching_parenthesis = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in matching_parenthesis:
            stack.append(char)
        elif char in matching_parenthesis.values():
            if not stack:
                return False  
            last_open = stack.pop() 
            if matching_parenthesis[last_open] != char:
                return False

    return not stack

expressions = [
    "( [ { } ] )",
    "{ [ ( ] ) }",
    "( [ ) ]",
    "( [ { } ] ( ) )"
]

for expr in expressions:
    result = are_parentheses_balanced(expr)
    print(f"Expression: {expr} is {'balanced' if result else 'not balanced'}")
