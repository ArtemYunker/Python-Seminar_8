import csv


def get_lists():
    with open('file1.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', )
        return list(reader)


def add_employees_to_list(employees):
    with open('file1.csv', 'a', encoding="utf8", newline='', ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(employees)


def update_employees(number, string):
    try:
        with open('file1.csv', 'r', encoding="utf8", newline='', ) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            data = list(reader)
            data[number] = string
        with open('file1.csv', 'w', encoding="utf8", newline='', ) as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for i in data:
                writer.writerow(i)
    except IndexError:
        print("Вы вышли за границы массива")
        exit()
    except Exception:
        print("Появились какие та другие ошибки")
        exit()


def delete(number):
    with open('file1.csv', 'r', encoding="utf8", newline='', ) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader)
        del data[number]
    with open('file1.csv', 'w', encoding="utf8", newline='', ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for i in data:
            writer.writerow(i)




def import_cvs():
    import csv
    array_cvs = []

    with open("file1.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        for i in file_reader:
            array_cvs.append(i)
    print(array_cvs)
    return (array_cvs)

def expot_txt(array_cvs):
    data = open ('file_ex.txt','w',encoding='utf-8')
    for i in range(len(array_cvs)):
        data.writelines(str(*array_cvs[i]) + '\n')

    data.close()
    return

def import_txt():
    new_array = []
    data = open('file_ex.txt', 'r',encoding='utf-8')
    for line in data:
        s = data.read().split()
        new_array.append(s)
    data.close()
    print(new_array)
    return new_array


def expot_csv(new_array):
    import csv
    array = str(*new_array).split()
    with open("file_ex.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = " ", lineterminator="\r")
        file_writer.writerow(["Фамилия", "Имя", "Телефон","Должность"])
        for i in range(len(array)):
            file_writer.writerow(array[i])
    return
