from datetime import datetime


class Event:
    def __init__(self, name, date_time, venue):
        self.name = name
        self.date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        self.venue = venue
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def display_event_details(self):
        print(f"Event: {self.name}")
        print(f"Date and Time: {self.date_time}")
        print(f"Venue: {self.venue}")
        print("Available Tickets:")
        for ticket in self.tickets:
            print(f" - {ticket}")

    def get_available_tickets(self):
        return [ticket for ticket in self.tickets if not ticket.is_sold_out()]
