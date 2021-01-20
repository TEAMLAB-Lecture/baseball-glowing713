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
    next_game = True
    print("Play Baseball")

    # ########
    # 3 스트라이크를 하고 다음 게임을 이어가지 않거나
    # 게임 도중 0을 입력할 때까지 게임은 무한 반복
    # #########
    while next_game:
        user_input = 999
        random_number = str(get_not_duplicated_three_digit_number())
        print("Random Number is : ", random_number)
        ######### 3 스트라이크가 나올 때까지 반복하는 부분 #########
        while True:
            user_input = input('Input guess number : ')
            # 게임 도중 0을 입력하면 즉시 종료
            if user_input == '0':
                break

            # 사용자의 올바른 입력 유도
            while not is_validated_number(user_input):
                print('Wrong Input, Input again')
                user_input = input('Input guess number : ')

            # 스트라이크, 볼 판정
            strike, ball = get_strikes_or_ball(user_input, random_number)
            print(f'Strikes : {strike} , Balls : {ball}')
            # 3 스트라이크에 종료
            if strike == 3 and ball == 0:
                break

        # 게임 도중에 사용자가 0을 입력해서 종료된 경우, 완전히 게임을 멈춘다.
        if user_input == '0':
            break

        ######### 다음 게임 진행 여부를 올바르게 입력할 때까지 반복하는 부분 #########
        next_game_str = ''
        while True:
            next_game_str = input('You win, one more(Y/N)?')
            if next_game_str == '0':
                break
            elif is_yes(next_game_str):
                next_game = True
                break
            elif is_no(next_game_str):
                next_game = False
                break
            else:
                print('Wrong Input, Input again')
        # 0을 입력받으면 완전히 종료한다.
        if next_game_str == '0':
            break
    print("Thank you for using this program")
    print("End of the Game")


if __name__ == "__main__":
    main()
