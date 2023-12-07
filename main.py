from venue import Venue
from event import Event
from ticket import Ticket

# Get Venue Information from User
venue_name = input("Enter the venue name: ")
venue_location = input("Enter the venue location: ")
venue = Venue(venue_name, venue_location)

# Get Event Information from User
event_name = input("Enter the event name: ")
event_date_time = input("Enter the event date and time (YYYY-MM-DD HH:mm): ")
event = Event(event_name, event_date_time, venue)

# Get Ticket Information from User
ticket_type1 = input("Enter ticket type 1: ")
ticket_price1 = float(input("Enter ticket price 1: "))
ticket_quantity1 = int(input("Enter ticket quantity 1: "))
ticket1 = Ticket(ticket_type1, ticket_price1, ticket_quantity1)

ticket_type2 = input("Enter ticket type 2: ")
ticket_price2 = float(input("Enter ticket price 2: "))
ticket_quantity2 = int(input("Enter ticket quantity 2: "))
ticket2 = Ticket(ticket_type2, ticket_price2, ticket_quantity2)

# Add Tickets to Event
event.add_ticket(ticket1)
event.add_ticket(ticket2)

# Display Event Details
event.display_event_details()

# Sell Tickets
ticket_to_sell = event.get_available_tickets()[0]
if ticket_to_sell.sell_ticket():
    print(f"Ticket sold successfully! Remaining quantity: {ticket_to_sell.quantity}")

# Display Updated Event Details
event.display_event_details()
