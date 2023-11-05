from logo import game_logo
from functions import check_user_input, print_loto, create_column

print(game_logo)

isValid_column_count = False
isValid_bachina_number = False
bachina_number = 0

while not isValid_column_count:
    column_count = input("Kaç kolon bulunmasını istiyorsunuz? ")
    isValid_column_count = check_user_input(column_count)

wants_bachina_number = input("Banko sayı istiyor musunuz? (e/evet h/hayır) ").lower()

while not isValid_bachina_number:
    match wants_bachina_number:
        case 'e' | 'evet':
            bachina_number = input("1-90 aralığında bir sayı giriniz: ")
            isValid_bachina_number = check_user_input(bachina_number)
            if 91 < int(bachina_number) or int(bachina_number) < 1:
                isValid_bachina_number = False
        case 'h' | 'hayır':
            break
        case _:
            wants_bachina_number = input("Lütfen geçerli bir yanıt giriniz: (e/evet h/hayır) ").lower()

column_count = int(column_count)
bachina_number = int(bachina_number)

number_count_in_column = 6

loto = create_column(column_count, number_count_in_column, bachina_number)

print_loto(loto)
