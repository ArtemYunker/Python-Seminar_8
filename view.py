def show_menu():
    print("Выберите команду :\n1 - показать всех сотрудников\n"
          "2 - добавить сотрудника\n3 - изменить данные сотрудника\n4 - удалить сотрудника\n"
          "5 - Импортировать из CSV файла\n6 - Экспортировать в TXT файл\n7 - Импортировать из TXT файл"
          "\n8 - Экспортировать в CSV файл")
    try:
        select = int(input())
        if not select in [1, 2, 3, 4, 5, 6, 7, 8]:
            raise ValueError
        return select
    except Exception:
        print("Всё пропало.")
        exit()


def show_employees(spisok):
    print("Список всех сотрудников :")
    for i, sotrudnik in enumerate(spisok):
        if i == 0:
            print(" ", *sotrudnik)
        else:
            print(i, *sotrudnik)


def add_employees():
    print("Введите Фамилию Имя Телефон и Должность через пробел: ")
    data = input().split()
    return data


def change_employees():
    print("Выберите строку для перезаписи: ")
    change = int(input())
    print("Введите строку для записи: ")
    string = input().split()
    return change, string


def delete():
    print("Напишите номер строки для удаления: ")
    number = int(input())
    return number
