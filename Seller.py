import re


class Salesman:

    # Инициализирую продавца
    def __init__(self, fio):
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


salesman = Salesman('Марина Сергеевна Петрова')
