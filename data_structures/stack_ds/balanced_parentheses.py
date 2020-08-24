from data_structures.stack_ds.stack import Stack


def balance_parentheses(symbol_string):
    struct = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "({[":
            struct.push(symbol)

        elif struct.isEmpty():
            balanced = False

        else:
            struct.pop()

        index += 1

    if balanced and struct.isEmpty():
        return True
    else:
        return False
