from data_structures.stack_ds.stack import Stack

"""In this program the aim is to convert an integer to binary digits using a 
simple algorithm - `Divide by 2`. The algorithm assumes that we start with an 
integer great than 0. A simple iteration continually divides the decimal 
number by 2 and keeps track of the remainder. The division by 2 keeps track 
of whether the number is an even or odd number. An even number will give a 
remainder of 0 and an odd number will give a remainder of 1. Building a 
sequence of the remainder we build up the values binary representation"""


def divide_by_2(dec_number):
    remstack = Stack()

    while dec_number > 0:
        rem = dec_number % 2
        remstack.push(rem)
        dec_number //= 2

    binary_str = ""
    while not remstack.isEmpty():
        binary_str += str(remstack.pop())

    return binary_str


print(divide_by_2(22))


def base_converter(dec_number, base):
    """takes in a number or string and the type of base it should be
    converted to."""
    chars = "0123456789ABECDEF"

    remainder_stack = Stack()

    while dec_number > 0:
        remainder = dec_number % base
        remainder_stack.push(remainder)
        dec_number //= base

    new_string = ""
    while not remainder_stack.isEmpty():
        new_string += chars[remainder_stack.pop()]

    return new_string


print(base_converter(233, 2))
