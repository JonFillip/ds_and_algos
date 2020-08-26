from data_structures.stack_ds.stack import Stack
import string


def infix_to_postfix(expression):
    """Takes an infix expression and converts it to a postfix expression"""
    precedence = {"^": 3, "*": 3, "/": 3, "%": 3, "+": 2, "-": 2, "(": 1}

    op_stack = Stack()
    postfix_list = []

    token_list = expression.split()

    for token in token_list:
        if token in string.ascii_uppercase or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.isEmpty()) and (precedence[op_stack.peek()]
                                                >= precedence[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.isEmpty():
        postfix_list.append(op_stack.pop())

    return "".join(postfix_list)


def infix_to_prefix(expression):
    """Takes an infix expression and converts it to a prefix expression"""
    precedence = {"^": 3, "*": 3, "/": 3, "%": 3, "+": 2, "-": 2, "(": 1}

    operator_stack = Stack()
    prefix_list = []

    token_list = expression.split()
    for token in token_list[::-1]:
        if token in string.ascii_uppercase or token in "0123456789":
            prefix_list.append(token)

        elif token == "(":
            operator_stack.push(token)
        elif token == ")":
            top_token = operator_stack.pop()
            while top_token != "(":
                prefix_list.append(top_token)
                top_token = operator_stack.pop()
        else:
            while (not operator_stack.isEmpty()) and (precedence[
                                                          operator_stack.peek()]
                                                      >= precedence[token]):
                prefix_list.append(operator_stack.pop())
            operator_stack.push(token)

    prefix_expr = infix_to_postfix("".join(prefix_list))

    return prefix_expr[::-1]


def convert():
    while True:
        expression = input("Enter an infix expression or 'exit' to quit "
                           "program: ")
        if expression.lower() == 'exit':
            break
        else:
            try:
                output = eval(expression)
            except NameError:
                output = expression

        print(f"Original expression is {expression}\n"
              f"Postfix expression: {infix_to_postfix(expression)}\n"
              f"Prefix expression: {infix_to_prefix(expression)}\n"
              f"Calculated result: {output}")


if __name__ == "__main__":
    convert()
