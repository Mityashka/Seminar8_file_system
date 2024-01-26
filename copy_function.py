from print_data import print_file

def copy_data():
    origin_file = int(input("Введите номер файла, из которого хотите скопировать строку: "))
    final_file = int(input("Введите номер файла, в который хотите скопировать строку: "))
    while origin_file + final_file != 3:
        print("Ошибка! Введите корректные номера файлов.")
        return copy_data

    print_file()
    with open(f'db/data_{origin_file}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки, которую хотите скопировать:\n "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    with open(f'db/data_{final_file}.txt', 'a', encoding='utf-8') as file_end:
        file_end.write(data[number_row - 1])
    print("Данные успешно скопированы!")

    

