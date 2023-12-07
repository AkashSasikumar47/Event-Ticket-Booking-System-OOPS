class Ticket:
    def __init__(self, ticket_type, price, quantity):
        self.ticket_type = ticket_type
        self.price = price
        self.quantity = quantity

    def is_sold_out(self):
        return self.quantity == 0

    def sell_ticket(self):
        if not self.is_sold_out():
            self.quantity -= 1
            return True
        else:
            print("Sorry, this ticket type is sold out.")
            return False

    def __str__(self):
        return f"{self.ticket_type} - ${self.price} - Quantity: {self.quantity}"
