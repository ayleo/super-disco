import pandas as pd


df = pd.read_csv('hotels.csv', dtype={'id': str})
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')
df_cards_security = pd.read_csv('card_security.csv', dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == hotel_id, 'name'].squeeze()
        self.capacity = df.loc[df['id'] == hotel_id, 'capacity'].squeeze()


    def book_room(self):
        """
        Book a room in the hotel and update the availability status to no
        Locate the hotel with the given id and update the availability status to no
        """
        df.loc[df['id'] == hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)
        print("Room booked successfully")

    def available_rooms(self):
        """Check if there are available rooms in the hotel"""
        availability = df.loc[df['id'] == hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object


    def confirm_reservation(self):
        content = f"""
        Dear {self.customer_name.capitalize()},
        Your reservation has been confirmed at hotel {self.hotel.name} 
        and contains a capacity of {self.hotel.capacity}.
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number


    def validate(self, expiry_date, holder, cvc):
        card_data = {"number": self.number, 
                     "expiration": expiry_date, 
                     "holder": holder, 
                     "cvc": cvc
                     }
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):

    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security['number'] == self.number, 'password'].squeeze()
        if password == given_password:
            return True
        else:
            return False


# Print the hotels and prompt the user for the hotel id
print(df)
hotel_id = input("Enter the hotel id: ")

# Create the hotel instance
hotel = Hotel(hotel_id)

# Check if there are available rooms and book a room
if hotel.available_rooms():

    credit_card = SecureCreditCard(number="1234567890123456")

    if credit_card.validate(expiry_date='12/26', holder="JOHN SMITH", cvc="123"):

        if credit_card.authenticate(given_password="mypass1"):

            hotel.book_room()
            name = input("Enter your name: ")
            ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(ticket.confirm_reservation())
        else:
            print("Credit card authentication failed. Invalid password")
    else:
        print("Failed to book room. Invalid credit card details.")
else:
    print("No rooms available")
