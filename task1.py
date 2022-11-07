import json


class Event:

    def __init__(self, name: str, date: str):
        self.name = name
        self.date = date
        self.sold_tickets = []

    def sell_ticket(self, ticket):
        self.sold_tickets.append(ticket)


class Ticket:

    def __init__(self, id_number: int, price: float, date: str, event: Event):
        self.id = id_number
        self.price = price
        self.date = date
        self.event = event
        self.add_ticket()

    def add_ticket(self):
        ticket = {
            "id": self.__id,
            "price": self.__price,
            "date": self.date,
            "event name": self.event.name,
            "event date": self.event.date,
        }
        with open('tickets.json', 'r+') as tickets_data:
            prev_tickets = json.load(tickets_data)
            for t in prev_tickets:
                if t['id'] == ticket['id']:
                    raise ValueError("Ticket with such id already exists")
            prev_tickets.append(ticket)
            tickets_data.seek(0)
            json.dump(prev_tickets, tickets_data)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_number: int):
        if not isinstance(id_number, int):
            raise TypeError("ticket id must be integer value")
        if id_number < 0:
            raise ValueError("ticket id must be >= 0")
        self.__id = id_number

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        if not isinstance(price, float) and not isinstance(price, int):
            raise TypeError("ticket price must be integer value")
        if price < 0:
            raise ValueError("ticket price must be >= 0")
        self.__price = price

    @staticmethod
    def ticket_info(id_number):
        with open('tickets.json', 'r') as tickets_data:
            tickets = json.load(tickets_data)
            for ticket in tickets:
                if ticket['id'] == id_number:
                    return f"Ticket number: {ticket['id']}\nticket price: ${ticket['price']}\ndate of purchase: " \
                           f"{ticket['date']}\nevent: {ticket['event name']}\nevent date: {ticket['event date']}"

    def __str__(self):
        return f"Ticket number: {self.id}\nticket price: ${self.price}\n" \
               f"date of purchase: {self.date}\nevent: {self.event.name}\nevent date: {self.event.date}"


class AdvanceTicket(Ticket):

    def __init__(self, id_number: int, price: float, date: str, discount: float, event: Event):
        discount_price = price * discount / 100
        super().__init__(id_number, price - discount_price, date, event)


class LateTicket(Ticket):

    def __init__(self, id_number: int, price: float, date: str, add_price: float, event: Event):
        additional_price = price + price * add_price / 100
        super().__init__(id_number, additional_price, date, event)


class StudentTicket(Ticket):

    def __init__(self, id_number: int, price: float, date: str, discount: float, event: Event):
        discount_price = price * discount / 100
        super().__init__(id_number, price - discount_price, date, event)


event1 = Event("All about freelance", "22.11.2022")
ticket2 = AdvanceTicket(1, 12, '02.11.2022', 40, event1)
ticket3 = LateTicket(2, 12, '02.11.2022', 40, event1)
ticket4 = StudentTicket(3, 12, '02.11.2022', 40, event1)
print(ticket4.ticket_info(3))
event1.sell_ticket(ticket2)
