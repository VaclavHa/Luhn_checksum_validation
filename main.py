# get user number
# double every other number from the end
# add values of all individuals digits
# if the sum is divisible by 10  => valid number else => NOT

def double(number_to_double: int) -> int:
    """
    Doubles the number and sums digits if result is 10 or more.

    :param number_to_double: odd number from inpuit number
    :return: doubled number or if number > 9 sum of doubled number digits
    """
    double_num = number_to_double * 2
    if double_num > 9:
        return double_num - 9
    else:
        return double_num


def check_for_valid(user_input: str) -> bool:
    """
    Sums even and odd(doubled) numbers together to validate the input number.

    :param user_input: number input by user
    :return: validation of the input number
    """
    total_sum = 0
    num_digits = len(user_input)
    for i, digit in enumerate(user_input):
        num = int(digit)
        if (num_digits - i) % 2 == 0:
            total_sum += double(num)
        else:
            total_sum += num

    if total_sum % 10 == 0:
        return True
    else:
        return False


def main():
    """
    Main function to get user input and validate it.

    :return: True if number is valid. False if not valid.
    """

    user_input = input('Enter a number: ')
    if not user_input.isdigit():
        print("Invalid input: Please enter only numeric digits")
        return False
    if check_for_valid(user_input):
        print('Number is valid!')
        return True
    else:
        print('Number IS NOT valid. Try again...')
        return False


if __name__ == '__main__':
    main()