import datetime as datetime


class Pizza:
    def __init__(self, name="Маргарита", dough="Традиционное",
                 sauce="Томатный", filling=["Томаты черри", "сыр Моцарелла", "Базилик"],
                 price=300, time_preparing=datetime.timedelta(minutes=30)):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.filling = filling
        self.price = price
        self.time_preparing = time_preparing
        self.new_price = self.price

        self.len_card = 62

        self.possible_doping = {"Кукуруза": 55, "Оливки": 65,
                                "Испанские Маслины": 40, "Ветчина": 90,
                                "Сыр Чеддер": 90, "Сыр Пармезан": 90,
                                "Шампиньоны Свежие": 70, "Опята": 70,
                                }

    def add_filling(self):  # метод добавление нового ингредиента
        print(f"\nСостав пиццы {self.name}: {self.print_list_composition(self.filling)}")

        print("Возможные добавки:")
        for key, val in self.possible_doping.items():
            print(f'- {key} - {val} руб.')
            # i += i

        res = input("\nХотите добавить новый ингредиент в пиццу? Цена будет изменена. да/нет\n->:").lower().strip()
        while res != "нет":
            if res == "да":
                filling = input("Введите ингредиент пиццы:\n->:").title().strip()

                if filling in self.possible_doping.keys():  # проверка на наличие в списке ингредиентов
                    self.filling.append(filling)  # добавление нового ингредиента в список
                    self.new_price += self.possible_doping[filling]  # повышение цены на каждый новый ингредиент
                    print(f"\nНовый состав пиццы {self.name}: {self.print_list_composition(self.filling)} \n")
                else:
                    print('У нас нет такой добавки')
                res = input("\nХотите добавить новый ингредиент в пиццу? Цена будет изменена. да/нет\n->:").lower().strip()
            else:
                print("Нет такой опции.")
                res = input("\nХотите добавить новый ингредиент в пиццу? Цена будет изменена. да/нет\n->:").lower().strip()

    def del_filling(self):  # метод удаления нового ингредиента

        res = input("\nХотите удалить ингредиент из пиццы? Цена будет изменена. да/нет\n->:").lower().strip()
        while res != "нет":
            if res == "да":
                print(f"\nСостав пиццы {self.name}: {self.print_list_composition(self.filling)}")
                del_item = input("\nВведите ингредиент для удаления: ").title().strip()
                if del_item in self.possible_doping.keys():  # если удаляемый элемент в списке дополнительных ингредиентов изменяем цену
                    self.filling.remove(del_item)  # удаление ингредиента из списка
                    if self.price <= self.new_price:  # если новая цена больше начальной
                        self.new_price -= self.possible_doping[del_item]  # уменьшение цены за каждый удаленный ингредиент
                    else:
                        self.new_price = self.price  # оставляем начальную цену
                    print(f"\nНовый состав пиццы {self.name}: {self.print_list_composition(self.filling)} \n")
                    res = input("\nХотите ещё удалить ингредиент? Цена будет изменена. да/нет\n->:").lower().strip()
                elif del_item in self.filling:  # если удаляемый элемент в основном списке ингредиентов изменяем цену
                    self.filling.remove(del_item)  # удаление  ингредиента из списка
                    print(f"\nНовый состав пиццы {self.name}: {self.print_list_composition(self.filling)} \n")
                    res = input("\nХотите ещё удалить ингредиент? Цена будет изменена. да/нет\n->:").lower().strip()
                else:
                    print(f'Такого ингредиента нет в составе {self.name}')
                    res = input("\nХотите удалить ингредиент? Цена будет изменена. да/нет\n->:").lower().strip()
            else:
                print("Нет такой опции.")
                res = input("\nХотите удалить ингредиент? Цена будет изменена. да/нет\n->:").lower().strip()

    def print_list(self, list):  # печать списка с заданным количеством элементов в строке
        n = 3  # количество элементов для вывода в строку
        h = []
        l = ""
        m = []
        for i in range(0, len(list), n):  # Разбиваем списка заданное количество элементов n
            h.append(list[i:i + n])

        for j in range(len(h)):
            if j == 0: # формируем первую строку
                l = '| Состоит из: '
                for r in h[j]:
                    l = l + r + ', '
                m.append(l)
            elif j == len(h)-1:  # удираем запятую и пробел у последней строки
                l = '|' + " " * 13
                for r in h[j]:
                    l = l + r + ', '
                l = l[:-2]
                m.append(l)
            else: # формируем промежуточные строки
                l = '|'+" " * 13
                for r in h[j]:
                    l = l + r + ', '
                m.append(l)
        return m

    def print_list_composition(self, list):
        l = ''
        for i in range(0, len(list)):
            # print(i)
            if (i + 1) % 4 == 0 and i != len(list) - 1:
                l = l + list[i] + ', ' + "\n"  # + ' '* 28
            elif i == len(list) - 1:
                l = l + list[i]
            else:
                l = l + list[i] + ', '
        return l

    def get_info(self):
        str_arr = [
            f"| *** {self.name} ***",
            f"| Готовится из {self.dough} теста.",
            f"| Соус - {self.sauce}.",
            f"| Время приготовления {self.time_preparing} минут.",
            f"| Цена {self.new_price} руб."
        ]

        fil_list = self.print_list(self.filling)  # форматированный массив ингредиентов

        k = 2  # индекс для вставки в str_arr
        for i in fil_list:  # добавляем форматированные строки ингредиентов в общий массив для вывода
            str_arr.insert(k, i)
            k += 1
        # печать карточки Пиццы
        print('+' + '-' * self.len_card + "+")
        for i in str_arr:
            l = len(i)
            print(i + " " * (self.len_card - l + 1) + "|")
        print('+' + '-' * self.len_card + "+")


class PizzaBBQ(Pizza):
    def __init__(self, name="Пицца Барбекю", dough="Традиционное", sauce="Барбекю",
                 filling=['Сыр Моцарелла', 'Говядина', 'Помидоры',
                          'Баклажаны', 'Шампиньоны', 'Сладкий Лук',
                          'Соленые Огурцы', 'Петрушка'],
                 price=654, time_preparing=datetime.timedelta(minutes=48)):
        super().__init__(name, dough, sauce, filling, price, time_preparing)

        self.possible_doping = {"Кукуруза": 55, "Оливки": 65,
                                "Испанские Маслины": 40, "Ветчина": 90,
                                "Грудинка": 90, "Куриная Грудка": 90,
                                "Охотничьи Колбаски": 95,
                                }


class PizzaPepperoni(Pizza):
    def __init__(self, name="Пицца Пепперони", dough="Тонкое", sauce="Томатный",
                 filling=['Салями Пепперони', 'Сыр Моцарелла', 'Томаты'],
                 price=520, time_preparing=datetime.timedelta(minutes=30)):
        super().__init__(name, dough, sauce, filling, price, time_preparing)

        self.possible_doping = {"Испанские Маслины": 40, "Ветчина": 90,
                                "Грудинка": 90, "Куриная Крудка": 90,
                                "Говядина": 90, "Охотничьи Колбаски": 95,
                                "Кунжут": 40,
                                }


class PizzaSeafood(Pizza):
    def __init__(self, name="Пицца с морепродуктами", dough="Традиционное",
                 sauce="Томатный",
                 filling=['Мидии', 'Кальмары', 'Креветки Отварные',
                          'Сыр Мацарелло', 'Лук Сладкий', 'Помидоры', 'Кукуруза'],
                 price=983, time_preparing=datetime.timedelta(minutes=36)):
        super().__init__(name, dough, sauce, filling, price, time_preparing)

        self.possible_doping = {"Оливки": 65,
                                "Испанские Маслины": 40, "Ветчина": 90,
                                "Итальянская Свиная Колбаса": 70, "Сыр Дорблю": 90,
                                "Сыр Чеддер": 90, "Сыр Пармезан": 90,
                                }