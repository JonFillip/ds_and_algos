from data_structures.stack_ds.stack import Stack
from search_sort_algo.binary_tree import BinaryTree
import operator

# 1. If the current token is a '(', it is added as the left child of the current
# node, and descend to the left child.
# 2. If the current_token is in the list [+, -, /, *], set the root value of
# the current node to the operator represented by the current token and add a
# new node as the right child of the current node and descend to the right
# child.
# 3. If the current_token is a number, set the root value of the current node
# to the number and return to the parent.
# 4. If the current_token is ')', go to the parent of the current node.


def equation_parser(expr):
    expr_list = expr.split()
    priority_stack = Stack()
    expr_tree = BinaryTree('')
    priority_stack.push(expr_tree)
    current_tree = expr_tree
    for token in expr_list:
        try:
            if token == '(':
                current_tree.insert_left('')
                priority_stack.push(current_tree)
                current_tree = current_tree.get_left_child()
            elif token not in '+-/*)':
                current_tree.set_root_value(eval(token))
                parent = priority_stack.pop()
                current_tree = parent
            elif token in '+-*/':
                current_tree.set_root_value(token)
                current_tree.insert_left('')
                priority_stack.push(current_tree)
                current_tree = current_tree.get_right_child()
            elif token == ') ':
                current_tree = priority_stack.pop()
        except ValueError:
            print(f"Unknown Operator: {token}")

    return expr_tree


def evaluate(parse_tree):
    operands = {'+': operator.add, '-': operator.sub, '*': operator.mul,
                '/': operator.truediv}

    left_subtree = parse_tree.get_left_child()
    right_subtree = parse_tree.get_right_child()

    if left_subtree and right_subtree:
        func = operands[parse_tree.get_root_val()]
        return func(evaluate(left_subtree), evaluate(right_subtree))
    else:
        return parse_tree.get_root_value()
