def question(question_str):
    user_input = input(question_str + "? Y/N\n").lower()
    if user_input == "y":
        return True
    else:
        return False


def check_type(inp, desired_type):
    if type(inp) == desired_type:
        return True
    else:
        return False


def check_even(num):
    if check_type(num, "int"):
        return False
    if num % 2 == 0:
        return True
    else:
        return False


