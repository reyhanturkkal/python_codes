from random import randint, shuffle
from logo import vertical_line, horizontal_line
def check_user_input(input):
    try:
        val = int(input)
    except ValueError:
        try:
            val = float(input)
        except ValueError:
            print("Lütfen bir sayı giriniz. ")
            return False
    return True

def print_loto(columns):
    for column in columns:
        print(horizontal_line)
        for number in column:
            print(' ' + str(number) + ' ', end=vertical_line)
    print(horizontal_line)


def create_column(column_count, number_count_in_column, bachina_number):
    columns = []

    for column_index in range(column_count):
        number_index = 0
        column = []

        if bachina_number != 0:
            number_index += 1
            column.append(bachina_number)

        while number_index < number_count_in_column:
            number = randint(1, 90)
            if number not in column:
                column.append(number)
                number_index += 1

        shuffle(column)
        columns.append(column)

    return columns