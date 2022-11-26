# Заказ #

from Pizza import Pizza, PizzaBBQ, PizzaPepperoni, PizzaSeafood

import datetime


class Order:
    def __init__(self):
        self.amount = []  # список с заказанными пиццами
        self.len_card = 52  # ширина чека
        self.order_creation_time = datetime.datetime.now()
        self.preparation_time = datetime.timedelta()

        self.total_pizzas_amount = 0
        self.total_price = 0

        self.readiness = False

    def find_preparation_time(self):
        biggest_time_preparing = max([pizza.time_preparing for pizza in self.amount])\
            if len(self.amount) > 0 else self.preparation_time
        self.preparation_time = biggest_time_preparing \
            if self.preparation_time < biggest_time_preparing else self.preparation_time

    def add_amount(self):  # метод добавления пицц
        add_amount = input('\nДобавить пиццу в заказ? да/нет\n'
                           '->: ').lower().strip()

        while add_amount != 'нет':
            if add_amount == 'да':
                select = input('\nКакую пиццу желаете выбрать?\n'
                               '1. "Маргарита" \n'
                               '2. "Барбекю" \n'
                               '3. "Пепперони" \n'
                               '4. "Пицца с морепродуктами" \n'
                               '->: ')

                def connect_file_pizza(a):
                    pizza = a
                    pizza.add_filling()
                    pizza.del_filling()
                    pizza.get_info()
                    self.amount.append(pizza)
                    self.total_pizzas_amount += 1
                    self.total_price += pizza.new_price
                    return pizza

                if select == '1':
                    connect_file_pizza(Pizza())
                elif select == '2':
                    connect_file_pizza(PizzaBBQ())
                elif select == '3':
                    connect_file_pizza(PizzaPepperoni())
                elif select == '4':
                    connect_file_pizza(PizzaSeafood())
                else:
                    print(f'Сделайте выбор согласно меню!')
            else:
                print('Выберите "да" или "нет"!')
            if add_amount == 'нет':
                print('Выбор закончен.')
                break
            add_amount = input('\nХотите добавить пиццу в заказ? да/нет\n'
                               '->: ').lower().strip()
        self.find_preparation_time()
        print('Ваш заказ:')
        self.show_orders()

    def show_orders(self):  # метод подсчета количества каждой заказанной пиццы
        self.readiness = True \
            if datetime.datetime.now() > self.order_creation_time + self.preparation_time else False

        def dist(x):
            distance = self.len_card - len(x)
            return distance

        print(f'+{"-" * self.len_card}+')
        total_pizza = f' Всего заказано пицц: {len(self.amount)} шт.'
        print(f'|{total_pizza}{" " * dist(total_pizza)}|\n'
              f'|{" " * self.len_card}|')

        pizza_amount = dict()
        pizza_cost = dict()

        for num in range(len(self.amount)):
            pizza_name = self.amount[num].name  # переменная, которая принимает пиццы из списка self.amount по имени
            cost = self.amount[num].new_price  # храним стоимость каждой пиццы
            if pizza_name in pizza_amount:
                pizza_amount[pizza_name] += 1
                pizza_cost[pizza_name] += cost
            else:
                pizza_amount[pizza_name] = 1
                pizza_cost[pizza_name] = cost

        for pizzas, pizza_sum in zip(pizza_amount.items(), pizza_cost.values()):
            output = f' {pizzas[0]} - {pizzas[1]} шт. - {pizza_sum} руб.'
            print(f'|{output}{" " * dist(output)}|')
        order_creation_time = f' Время заказа: {self.order_creation_time.strftime("%d-%m-%y %H:%M:%S")}'
        ready_time = self.order_creation_time + self.preparation_time
        order_preparation_time = f' Время готовности:' \
                                 f' {ready_time.strftime("%d-%m-%y %H:%M:%S") if self.readiness is False else "Ваш заказ готов."}'
        total_price_string = f' Сумма: {self.total_price} р.'
        print(f'|{" " * self.len_card}|\n'
              f'|{total_price_string}{" " * dist(total_price_string)}|\n'
              f'|{" " * self.len_card}|\n'
              f'|{order_creation_time}{" " * dist(order_creation_time)}|\n'
              f'|{order_preparation_time}{" " * dist(order_preparation_time)}|\n'
              f'+{"-" * self.len_card}+')


# x = Order()
# x.add_amount()