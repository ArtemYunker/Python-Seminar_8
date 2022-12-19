import view
import models
import logging

# если хотим, чтобы логи записывались в файл
# logging.basicConfig (filename='log.txt',
#                     filemode='a',
#                     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#                     datefmt='%H:%M:%S',
#                     level=logging.DEBUG, encoding="UTF-8")


def main():
    select = view.show_menu()
    if select == 1:
        logging.info("Выбран 1")
        sotr = models.get_lists()
        view.show_employees(sotr)
        logging.info("Всё сработало.")
    elif select == 2:
        logging.warning("Выбран 2")
        data = view.add_employees()
        models.add_employees_to_list(data)
        logging.warning("Всё сработало.")
    elif select == 3:
        change, string = view.change_employees()
        print(change, string)
        models.update_employees(change, string)
    elif select == 4:
        logging.warning("выбран 4")
        number = view.delete()
        models.delete(number)
        logging.warning("Всё сработало.")
    elif select == 5:
        logging.info("Выбран 5")
        array_cvs = models.import_cvs()
        print(len(array_cvs))
    elif select == 6:
        logging.info("Выбран 6")
        array_cvs = models.import_cvs()
        models.expot_txt(array_cvs)
    elif select == 7:
        logging.info("Выбран 7")
        models.import_txt()
    elif select == 8:
        logging.info("Выбран 8")
        new_array=models.import_txt()
        models.expot_csv(new_array)
    else:
        print("Всё пропало!")
    logging.info("Всё сработало!")