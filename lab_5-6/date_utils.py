# date_utils.py

"""
Цель этой лабораторной работы - разработка модуля date_utils для работы с датами.

Модуль предоставляет следующие функции:
1. format_current_date(format_str="%Y-%m-%d %H:%M:%S"):
   Функция форматирует текущую дату и время с использованием заданного формата.

   Параметры:
   - format_str (str): Строка формата для datetime.strftime (по умолчанию "%Y-%m-%d %H:%M:%S").

   Возвращает:
   - str: Отформатированная строка текущей даты и времени.

2. calculate_date_difference(start_date, end_date):
   Функция вычисляет разницу между двумя датами.

   Параметры:
   - start_date (datetime.datetime): Начальная дата.
   - end_date (datetime.datetime): Конечная дата.

   Возвращает:
   - datetime.timedelta: Объект timedelta, представляющий разницу между датами.
"""


from datetime import datetime, timedelta

def format_current_date(format_str="%Y-%m-%d %H:%M:%S"):
    """
    Функция форматирует текущую дату и время с использованием заданного формата.

    :param format_str: Строка формата для datetime.strftime (по умолчанию "%Y-%m-%d %H:%M:%S").
    :type format_str: str
    :return: Отформатированная строка текущей даты и времени.
    :rtype: str
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime(format_str)
    return formatted_date

def calculate_date_difference(start_date, end_date):
    """
    Функция вычисляет разницу между двумя датами.

    :param start_date: Начальная дата.
    :type start_date: datetime.datetime
    :param end_date: Конечная дата.
    :type end_date: datetime.datetime
    :return: Объект timedelta, представляющий разницу между датами.
    :rtype: datetime.timedelta
    """
    date_difference = end_date - start_date
    return date_difference

if __name__ == "__main__":
    formatted_date = format_current_date()
    print("Formatted Date:", formatted_date)

    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 15)
    date_diff = calculate_date_difference(start_date, end_date)
    print("Date Difference:", date_diff)