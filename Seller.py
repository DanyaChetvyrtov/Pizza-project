import datetime
import re


class Salesman:
    # Статические свойства
    time_open = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
    time_close = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

    # Инициализирую продавца
    def __init__(self, fio):
        # Проверяем продавца в момент инициализации
        self.verify_fio(fio)
        self.fio = fio

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

    # Замена Данных ФИО если меняется продавец
    @property
    def seller_fio(self):
        return self.fio

    @seller_fio.setter
    def seller_fio(self, fio):
        self.verify_fio(fio)
        self.fio = fio

    # Открываем кассу
    def open_cash(self):
        return f'Кассу открыла/л: {self.fio} {Salesman.time_open}.'

    # Закрываем кассу
    def close_cash(self):
        return f'Кассу закрыла/л: {self.fio} {Salesman.time_close}.'


salesman = Salesman('Марина Сергеевна Петрова')
print(salesman.fio)
# Открываем кассу
print(salesman.open_cash())
# Если хотим поменять продавца во время смены или до смены.
salesman.seller_fio = 'Пушкин Роман Сергеевич'
print(salesman.seller_fio)
# Закрываем кассу
print(salesman.close_cash())