# Function to convert a string to a yes or no question, then returns if it is true or not
def question(question_str):
    user_input = input(question_str + "? Y/N\n").lower()
    if user_input == "y":
        return True
    else:
        return False


# compares the type of the input to the desired type, returning true if is the type and false if it is not
def check_type(inp, desired_type):
    if type(inp) == desired_type:
        return True
    else:
        return False


# Checks if an integer is even by dividing it by 2 and using the remainder to check it (0 if even, 1 if odd)
def check_even(num):
    if check_type(num, "int"):
        return False
    if num % 2 == 0:
        return True
    else:
        return False


# Converts two lists into a dictionary
def two_list_to_dict(lst1, lst2):
    end_dict = {}
    for entry in range(len(lst1)):
        end_dict[lst1[entry]] = lst2[entry]
    return end_dict


