# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    # 입력받은 숫자 문자열 중 digit이 아닌 것이 존재하면 정수로 변환 불가능하다고 판정
    for i in range(len(user_input_number)):
        if not user_input_number[i].isdigit():
            return False
    return True


def is_between_100_and_999(user_input_number):
    if len(user_input_number) == 3:
        return True
    else:
        return False


def is_duplicated_number(three_digit):
    if three_digit[0] == three_digit[1] or three_digit[0] == three_digit[2] or three_digit[1] == three_digit[2]:
        return True
    else:
        return False


def is_validated_number(user_input_number):
    if is_digit(user_input_number) and is_between_100_and_999(user_input_number) and not is_duplicated_number(user_input_number):
        return True
    else:
        return False


def get_not_duplicated_three_digit_number():
    # is_duplicated_number 함수를 사용하여 중복되는 값이 없는 숫자를 찾을 때까지
    # get_random_number 함수로 난수를 받아온다.
    random_num = get_random_number()
    while is_duplicated_number(str(random_num)):
        random_num = get_random_number()
    return random_num


def get_strikes_or_ball(user_input_number, random_number):
    result = [0, 0]  # [strikes, balls]
    for number in user_input_number:
        if number in random_number:
            if user_input_number.index(number) is random_number.index(number):
                result[0] += 1
            else:
                result[1] += 1
    return result


def is_yes(one_more_input):
    one_more_input = one_more_input.lower()
    if one_more_input == 'y' or one_more_input == 'yes':
        return True
    else:
        return False


def is_no(one_more_input):
    one_more_input = one_more_input.lower()
    if one_more_input == 'n' or one_more_input == 'no':
        return True
    else:
        return False


def main():
    print("Play Baseball")

    The_end = False
    while True:
        user_input = 999
        random_number = str(get_not_duplicated_three_digit_number())
        print("Random Number is : ", random_number)

        while user_input != random_number:
            user_input = input('Input guess number : ')
            if user_input == "0":
                The_end = True
                break

            if is_validated_number(user_input) == False:
                print("Wrong Input, Input again")
                continue

            result = list()
            result = get_strikes_or_ball(user_input, random_number)
            print(f"Strikes : {result[0]} , Balls : {result[1]}")

        if The_end:
            break

        while True:
            one_more_time = input("You win, one more(Y/N)?")
            if is_yes(one_more_time) or is_no(one_more_time):
                break
            print("Wrong Input, Input again")

        if is_yes(one_more_time):
            continue
        elif is_no(one_more_time):
            break

    # ==================================
    print("Thank you for using this program")
    print("End of the Game")


if __name__ == "__main__":
    main()
