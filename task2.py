class Pizza:
    toppings_prices = {
        'Tomato sauce': 2,
        'Mozzarella': 3,
        'Onions': 2,
        'Oregano': 1,
        'Eggplants': 0.85,
        'Artichokes': 0.5,
        'Garlic': 0.75,
        'Basil': 0.85,
        'Hot Italian salami': 1,
        'Hot chili peppers': 1.1,
        'Clams': 1.2,
        'Pecorino Romano': 1.3,
        'Olive oil': 1.25,
        'Cheese': 1.5,
        'Pineapple': 1.6,
        'Ham': 1.8,
        'Salami': 0.7,
        'Meatballs': 1.8,
        'Habanero peppers': 1.3,
    }

    def __init__(self, toppings: list):
        self.price = 0
        self.toppings = toppings
        self.calculate_price()

    def calculate_price(self):
        for ingredient in self.toppings:
            self.price += self.toppings_prices[ingredient]

    def add_topping(self, topping: str):
        if not (topping in self.toppings_prices):
            raise ValueError('There isn`t such topping')
        self.toppings.append(topping)
        self.price += self.toppings_prices[topping]


class Cipolla(Pizza):

    def __init__(self):
        super().__init__(['Tomato sauce', 'Mozzarella', 'Onions', 'Oregano'])


class Contadina(Pizza):

    def __init__(self):
        super().__init__(['Tomato sauce', 'Mozzarella', 'Eggplants', 'Artichokes', 'Garlic', 'Basil'])


class Diavola(Pizza):

    def __init__(self):
        super().__init__(['Tomato sauce', 'Mozzarella', 'Hot Italian salami', 'Hot chili peppers'])


class Apizza(Pizza):

    def __init__(self):
        super().__init__(['Clams', 'Pecorino Romano', 'Garlic', 'Olive oil', 'Oregano'])


class Hawaii(Pizza):

    def __init__(self):
        super().__init__(['Tomato sauce', 'Cheese', 'Pineapple', 'Ham'])


class Meatball(Pizza):

    def __init__(self):
        super().__init__(['Tomato sauce', 'Cheese', 'Salami', 'Meatballs'])


class Habanero(Pizza):

    def __init__(self):
        super().__init__(['Tomato sauce', 'Cheese', 'Habanero peppers'])
