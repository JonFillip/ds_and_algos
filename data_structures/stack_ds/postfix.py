from data_structures.stack_ds.stack import Stack
import string


def infix_to_postfix(expression):
    """Takes an infix expression and converts it to a postfix expression"""
    precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    op_stack = Stack()
    postfix_list = []

    token_list = expression.split()

    for token in token_list:
        if token in string.ascii_uppercase:
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.isEmpty()) and (precedence[op_stack.peek()] >= precedence[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.isEmpty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)


print(infix_to_postfix("( A + B ) * ( C + D )"))
print(infix_to_postfix("( A * C ) - B"))
