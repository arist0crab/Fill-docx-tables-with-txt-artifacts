from colors import Colors
from configurations import *


def greeting():
    """
    Allows you to check the operating mode of program
    """
    print(f"{Colors.GREEN}Включить инструктаж? [n/y]:{Colors.ENDC}", end=' ')
    if input().strip() == 'y':
        sources_warning()
        wait_to_ans()
        configuration_warning()
        wait_to_ans()
    print_current_configurations()

    return input().strip() == 'y'


def configuration_warning():
    print()
    print(
        f"{Colors.YELLOW}Чтобы изменить настройки текущей сессии, "
        f"настоятельно рекомендую\nпосетить файл 'configuration.py' и "
        f"изменить в нем значения под свой запрос.\nНе забудьте "
        f"перезапустить сессию, если настройки будут изменены.{Colors.ENDC}"
    )
    print()


def sources_warning():
    print()
    print(
        f"{Colors.YELLOW}Информация для заполнения таблиц берется из txt-файлов.\n"
        "Пример организации:"
    )
    print()
    print("=====txt=====            ====table====")
    print("A     B     C            | A | B | C |")
    print("4     5     6     ->     | 4 | 5 | 6 |")
    print("7     8     8            | 7 | 8 | 8 |")
    print("9     0     9            | 9 | 0 | 9 |")
    print()
    print(
        f"Ваши txt-файлы должны лежать в папке 'sources' "
        f"в том порядке, в котором\nрасположены таблицы в вашем документе. "
        f"Названия txt-файлов не играют роли,\nглавное, чтобы их алфавитный "
        f"порядок соответствовал порядку таблиц.{Colors.ENDC}"
    )
    print()


def print_current_configurations():
    print()
    print(f"{Colors.YELLOW}==============Текущие настройки==============")
    free_space = 45 - 19 - len(str(TABLES_QUANTITY))
    print(f"Таблиц в документе:" + free_space * '.' + f"{TABLES_QUANTITY}")
    free_space = 45 - 34 - (2 if REPLACE_TABLES_HEADERS else 3)
    print(f"Заменить заголовки в таблице(-ах):" + free_space * '.' + f"{"да" if REPLACE_TABLES_HEADERS else "нет"}")
    print()
    print(f"{Colors.GREEN}Подтвердите настройки [n/y]:{Colors.ENDC}", end=' ')


def wait_to_ans():
    print("Нажмите любую кнопку чтобы продолжить ->", end=' ')
    input()
