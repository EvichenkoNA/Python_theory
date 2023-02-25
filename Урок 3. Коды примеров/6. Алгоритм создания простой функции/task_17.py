"""Многострочники"""

"""
1) Определить название функции. Оно должно быть информативным,
чтобы было понятно назначение функции.
"""

"""
2) Определить в строках документации назначение функции,
типы данных ее параметров и тип данных результата.
Можно также указать пример вызова функции с параметром и возвращаемый результат.
"""

"""
3) Определить информативные имена параметров, передаваемых в функцию,
написать тело функции с возвращаемым результатом (при необходимости).
"""


def rectangle_area_calc(length, width):
    """
    Возвращает площадь прямоугольника по длине и ширине

    (number, number) -> number

    >>> rectangle_area_calc(10, 10)
    100
    """
    return length * width
