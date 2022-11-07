from datetime import datetime


def get_pizza(day_of_week, pizza_schedule):
    import task2
    pizza_name = pizza_schedule[day_of_week]
    pizza_obj = getattr(task2, pizza_name)
    return pizza_obj()


if __name__ == '__main__':
    pizzas_schedule = {}
    with open("menu.txt", 'r') as menu:
        for line in menu:
            day, pizza = line.split(':')
            pizzas_schedule[int(day)] = pizza.strip()
    pizza_of_the_day = get_pizza(datetime.now().weekday(), pizzas_schedule)
    print(pizza_of_the_day.price)
