from data_structures.stack_ds.stack import Stack


def postfix_eval(expression):
    oper_stack = Stack()

    token_list = expression.split()

    for token in token_list:
        if token in "0123456789":
            oper_stack.push(int(token))
        else:
            operand2 = oper_stack.pop()
            operand1 = oper_stack.pop()
            result = do_math(token, operand1, operand2)
            oper_stack.push(result)

    return oper_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
