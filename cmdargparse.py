import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help="first number")
    parser.add_argument("number2", help="second number")
    parser.add_argument("--operation", help="operation")  # optional

    arg = parser.parse_args()

    print(arg.number1, arg.number2, arg.operation)

    n1, n2 = int(arg.number1), int(arg.number2)

    if arg.operation == "+":
        print(n1 + n2)

    # python cmdargparse.py -h

    """
        two types of args:
        -  positional args
        -  optional
    """
