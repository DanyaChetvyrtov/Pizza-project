import re
import datetime


# Класс Продавец
class Salesman:
    time_open = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
    time_close = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

    # Инициализируем продавца
    def __init__(self, fio):
        self.verify_fio(fio)
        self.fio = fio
        # print('*' * 50)

    # Верификация проверки имени, фамилии, отчества
    @classmethod
    def verify_fio(cls, fio):
        if not isinstance(fio, str):
            # выбрасываем исключение если неправильно введен тип.
            raise TypeError('ФИО должно быть строкой')
        data_fio = fio.split()
        # Пользователь не должен ввести больше или меньше трех значений.
        if len(data_fio) != 3:
            raise TypeError('Неверный формат ФИО')
        # Проверяем что бы не было - и были введены только буквы.
        letters = ''.join(re.findall(r'[а-яё-]', fio, flags=re.IGNORECASE))
        for data in data_fio:
            if len(data.strip(letters)) != 0:
                raise TypeError('В ФИО можно использовать только буквы и дефис')

    @property
    def seller_fio(self):
        return self.fio

    @seller_fio.setter
    def seller_fio(self, fio):
        self.verify_fio(fio)
        self.fio = fio

    # Открываем кассу
    # def open_cash(self):
    #     return f'Кассу открыла/л: {self.fio} {Salesman.time_open}.'

    # Закрываем кассу
    # def close_cash(self):
    #     return f'Кассу закрыла/л: {self.fio} {Salesman.time_close}.'

    # в данный метод нужно дописать данные чека и сумму, которая была за день.
    # def print_check(self):
    #     print(f'Чек: {self.fio}\n '
    #           f'время открытия кассы:{self.time_open} '
    #           f'время закрытия кассы: {self.time_close}\n '
    #           f'общая сумма: {}')

#
# # экземпляр класса. Имена выдуманные.
# salesman = Salesman('Марина Сергеевна Петрова')
# # print(salesman.fio)
# # Открываем кассу
# print(salesman.open_cash())
# # Если хотим поменять продавца во время смены или до смены.
# salesman.seller_fio = 'Пушкин Роман Сергеевич'
# # Закрываем кассу
# print(salesman.close_cash())
# # чек за день
# # salesman.print_check()
