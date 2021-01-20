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
    while next_game:
        user_input = 999    # 사용자 입력 초기화

        # 맞춰야 할 랜덤 숫자 할당
        random_number = str(get_not_duplicated_three_digit_number())
        print("Random Number is : ", random_number)  # 할당된 랜덤 숫자 출력

        while True:
            user_input = input('Input guess number : ')
            # <특수조건> 사용자가 게임 중 0을 입력하면 게임을 종료해야 한다.
            if user_input == '0':
                next_game = False
                break

            # 잘못된 숫자를 입력했다면 오류메세지 출력하고 다시 입력을 받는다.
            if not is_validated_number(user_input):
                print('Wrong Input, Input again')

            # 제대로 입력. 야구게임 연산 시작
            else:

                strike, ball = get_strikes_or_ball(user_input, random_number)
                if strike == 3 and ball == 0:
                    # 정답을 맞춤
                    want_next = input('You win, one more(Y/N)?')
                    # <특수조건> 사용자가 게임 중 0을 입력하면 게임을 종료해야 한다.
                    if user_input == '0':
                        next_game = False
                        break
                    # 게임을 더 할 의향이 있는지 물어보기. 문법 틀리게 입력하면 다시 입력받기.
                    while True:
                        # <특수조건> 사용자가 게임 중 0을 입력하면 게임을 종료해야 한다.
                        if want_next == '0':
                            next_game = False
                            break
                        elif is_yes(want_next):
                            next_game = True
                            break
                        elif is_no(want_next):
                            next_game = False
                            break
                        else:
                            print('Wrong Input, Input again')
                            want_next = input('You win, one more(Y/N)?')
                    break

                else:
                    print(f'Strikes : {strike} , Balls : {ball}')

    print("Thank you for using this program")
    print("End of the Game")


if __name__ == "__main__":
    main()
