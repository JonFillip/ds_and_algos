from data_structures.stack_ds.stack import Stack

# Using recursive function to convert any given integer to a string in
# specified base from 2 to 16.

stack = Stack()


def convstr(value, base):
    convert_string = "0123456789ABECDEF"
    if value < base:
        return stack.push(convert_string[value])
    else:
        stack.push(convert_string[value % base])
        convstr(value // base, base)


def main():
    while True:
        print("Please enter an integer and base you wish to convert the "
              "integer between base 2 - 16 or enter 'quit' to leave program: ")
        value = input("Enter integer: ")
        base = input("Enter base: ")
        if value.lower() == 'quit' or base.lower() == 'quit':
            break
        else:
            return f"{value} converted to base{base} is " \
                   f"{convstr(int(value), int(base))}"


if __name__ == "__main__":
    print(main())
