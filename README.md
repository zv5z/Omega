room.py:
class Room:
    """
    Represents a hotel room with attributes such as price, amenities, and availability.
    """
    def __init__(self, room_number, price_per_night, amenities, is_available=True):
        """
        Initializes a Room instance.
        :param room_number: Unique identifier for the room.
        :param price_per_night: Cost per night for staying in the room.
        :param amenities: List of amenities available in the room.
        :param is_available: Availability status of the room.
        """
        self._room_number = room_number
        self._price_per_night = price_per_night
        self._amenities = amenities
        self._is_available = is_available

    def get_room_number(self):
        """Returns the room number."""
        return self._room_number

    def get_price_per_night(self):
        """Returns the price per night for the room."""
        return self._price_per_night

    def set_price_per_night(self, price):
        """Sets the price per night for the room."""
        self._price_per_night = price

    def get_amenities(self):
        """Returns the list of amenities available in the room."""
        return self._amenities

    def set_amenities(self, amenities):
        """Sets the list of amenities available in the room."""
        self._amenities = amenities

    def get_is_available(self):
        """Returns the availability status of the room."""
        return self._is_available

    def set_is_available(self, is_available):
        """Sets the availability status of the room."""
        self._is_available = is_available

    def update_availability(self, status):
        """Updates the room's availability status."""
        self._is_available = status

    def __str__(self):
        return f"Room {self._room_number}: ${self._price_per_night}/night, Available: {self._is_available}"

class SingleRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, 100, ["WiFi", "TV", "Air Conditioning"])

class DoubleRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, 150, ["WiFi", "TV", "Mini Fridge", "Air Conditioning"])

class Suite(Room):
    def __init__(self, room_number):
        super().__init__(room_number, 300, ["WiFi", "TV", "Mini Fridge", "Jacuzzi", "Living Area"])

class Booking:
    """
    Represents a hotel room booking.
    """
    def __init__(self, guest, room, check_in_date, check_out_date, booking_id):
        """
        Initializes a new booking.
        :param guest: Guest object, the guest making the booking
        :param room: Room object, the room being booked
        :param check_in_date: str, check-in date
        :param check_out_date: str, check-out date
        :param booking_id: str, unique booking identifier
        """
        self._guest = guest
        self._room = room
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._booking_id = booking_id
        self._payment = None
        self._invoice = None

    def get_guest(self):
        """Returns the guest associated with the booking."""
        return self._guest

    def get_room(self):
        """Returns the room associated with the booking."""
        return self._room

    def get_check_in_date(self):
        """Returns the check-in date."""
        return self._check_in_date

    def get_check_out_date(self):
        """Returns the check-out date."""
        return self._check_out_date

    def get_booking_id(self):
        """Returns the booking ID."""
        return self._booking_id

    def set_payment(self, payment):
        """Assigns a payment method to the booking."""
        self._payment = payment

    def generate_invoice(self):
        """Generates an invoice for the booking."""
        nights = (self._check_out_date - self._check_in_date).days
        total = nights * self._room.get_price_per_night()
        self._invoice = {"total": total, "payment_method": self._payment}
        return self._invoice

    def __str__(self):
        return f"Booking ID: {self._booking_id}, {self._room} from {self._check_in_date} to {self._check_out_date}"

guest.py
class Guest:
    """
    Represents a hotel guest with personal details and booking history.
    """
    def __init__(self, guest_id, name, email, contact, loyalty_account):
        """
        Initializes a Guest instance.
        :param guest_id: Unique identifier for the guest.
        :param name: Guest's full name.
        :param email: Guest's email address.
        :param contact: Guest's contact number.
        :param loyalty_account: Loyalty account associated with the guest.
        """
        self._guest_id = guest_id
        self._name = name
        self._email = email
        self._contact = contact
        self._loyalty_account = loyalty_account
        self._bookings = []

    def get_name(self):
        """Returns the guest's name."""
        return self._name

    def set_name(self, name):
        """Sets the guest's name."""
        self._name = name

    def get_email(self):
        """Returns the guest's email."""
        return self._email

    def set_email(self, email):
        """Sets the guest's email."""
        self._email = email

    def get_contact(self):
        """Returns the guest's contact number."""
        return self._contact

    def set_contact(self, contact):
        """Sets the guest's contact number."""
        self._contact = contact

    def make_booking(self, booking):
        """Adds a booking to the guest's reservation history."""
        self._bookings.append(booking)

    def view_reservation_history(self):
        """Returns the guest's booking history."""
        return self._bookings

    def __str__(self):
        return f"Guest {self._name} ({self._email})"

class LoyaltyAccount:
    """
    Represents a guest's loyalty account, tracking points and tier status.
    """
    def __init__(self, account_id, points, tier, last_updated):
        """
        Initializes a LoyaltyAccount instance.
        :param account_id: Unique identifier for the loyalty account.
        :param points: Number of loyalty points.
        :param tier: Loyalty tier status.
        :param last_updated: Last update timestamp for the account.
        """
        self._account_id = account_id
        self._points = points
        self._tier = tier
        self._last_updated = last_updated

    def get_points(self):
        """Returns the number of loyalty points."""
        return self._points

    def set_points(self, points):
        """Sets the number of loyalty points."""
        self._points = points

    def get_tier(self):
        """Returns the loyalty tier."""
        return self._tier

    def set_tier(self, tier):
        """Sets the loyalty tier."""
        self._tier = tier

    def get_last_updated(self):
        """Returns the last updated timestamp."""
        return self._last_updated

    def set_last_updated(self, last_updated):
        """Sets the last updated timestamp."""
        self._last_updated = last_updated

    def earn_points(self, amount):
        """Adds points to the loyalty account."""
        self._points += amount

    def redeem_points(self, amount):
        """Redeems points from the loyalty account if sufficient balance is available."""
        if amount <= self._points:
            self._points -= amount
        else:
            raise ValueError("Insufficient points to redeem.")

    def __str__(self):
        return f"Loyalty Account {self._account_id}: {self._points} points, Tier: {self._tier}"


booking.py
from datetime import date
from abc import ABC, abstractmethod

class Room:
    """
    Represents a hotel room with attributes such as price, amenities, and availability.
    """
    def __init__(self, room_number, price_per_night, amenities, is_available=True):
        self._room_number = room_number
        self._price_per_night = price_per_night
        self._amenities = amenities
        self._is_available = is_available

    def get_room_number(self):
        return self._room_number

    def get_price_per_night(self):
        return self._price_per_night

    def set_price_per_night(self, price):
        self._price_per_night = price

    def get_amenities(self):
        return self._amenities

    def set_amenities(self, amenities):
        self._amenities = amenities

    def get_is_available(self):
        return self._is_available

    def set_is_available(self, is_available):
        self._is_available = is_available

    def update_availability(self, status):
        self._is_available = status

    def __str__(self):
        return f"Room {self._room_number}: ${self._price_per_night}/night, Available: {self._is_available}"

class SingleRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, 100, ["WiFi", "TV", "Air Conditioning"])

class DoubleRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, 150, ["WiFi", "TV", "Mini Fridge", "Air Conditioning"])

class Suite(Room):
    def __init__(self, room_number):
        super().__init__(room_number, 300, ["WiFi", "TV", "Mini Fridge", "Jacuzzi", "Living Area"])

class Booking:
    """
    Represents a hotel room booking.
    """
    def __init__(self, guest, room, check_in_date, check_out_date, booking_id):
        self._guest = guest
        self._room = room
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._booking_id = booking_id
        self._payment = None
        self._invoice = None

    def get_guest(self):
        return self._guest

    def get_room(self):
        return self._room

    def get_check_in_date(self):
        return self._check_in_date

    def get_check_out_date(self):
        return self._check_out_date

    def get_booking_id(self):
        return self._booking_id

    def set_payment(self, payment):
        self._payment = payment

    def generate_invoice(self):
        nights = (self._check_out_date - self._check_in_date).days
        total = nights * self._room.get_price_per_night()
        self._invoice = {"total": total, "payment_method": self._payment}
        return self._invoice

    def __str__(self):
        return f"Booking ID: {self._booking_id}, {self._room} from {self._check_in_date} to {self._check_out_date}"

class ServiceRequest:
    """
    Represents a service request made by a hotel guest.
    """
    def __init__(self, request_type, details, status="Pending", request_date=None):
        self._request_type = request_type
        self._details = details
        self._status = status
        self._request_date = request_date or date.today()

    def __str__(self):
        return f"{self._request_type}: {self._details} ({self._status}), Date: {self._request_date}"

class Feedback:
    """
    Represents guest feedback for hotel services.
    """
    def __init__(self, rating, comments, guest_name, feedback_date):
        self._rating = rating
        self._comments = comments
        self._guest_name = guest_name
        self._feedback_date = feedback_date

    def __str__(self):
        return f"Feedback by {self._guest_name} on {self._feedback_date}: {self._rating}/5 - {self._comments}"

class Payment(ABC):
    """
    Abstract base class for different payment methods.
    """
    def __init__(self, amount, payment_date, transaction_id):
        self._amount = amount
        self._payment_date = payment_date
        self._transaction_id = transaction_id

    @abstractmethod
    def process_payment(self):
        pass

    def __str__(self):
        return f"Payment of ${self._amount} on {self._payment_date}, Transaction ID: {self._transaction_id}"

class CreditCardPayment(Payment):
    """
    Handles credit card payment processing.
    """
    def __init__(self, amount, card_number, expiry_date, payment_date, transaction_id):
        super().__init__(amount, payment_date, transaction_id)
        self._card_number = card_number
        self._expiry_date = expiry_date

    def process_payment(self):
        return f"Paid ${self._amount} via Credit Card on {self._payment_date}"

class MobileWalletPayment(Payment):
    """
    Handles mobile wallet payment processing.
    """
    def __init__(self, amount, wallet_type, phone_number, payment_date, transaction_id):
        super().__init__(amount, payment_date, transaction_id)
        self._wallet_type = wallet_type
        self._phone_number = phone_number

    def process_payment(self):
        return f"Paid ${self._amount} via {self._wallet_type} on {self._payment_date}"




services.py
from datetime import date

class Room:
    """
    Represents a hotel room with attributes such as price, amenities, and availability.
    """
    def __init__(self, room_number, price_per_night, amenities, is_available=True):
        """
        Initializes a Room instance.
        :param room_number: Unique identifier for the room.
        :param price_per_night: Cost per night for staying in the room.
        :param amenities: List of amenities available in the room.
        :param is_available: Availability status of the room.
        """
        self._room_number = room_number
        self._price_per_night = price_per_night
        self._amenities = amenities
        self._is_available = is_available

    def get_room_number(self):
        """Returns the room number."""
        return self._room_number

    def get_price_per_night(self):
        """Returns the price per night for the room."""
        return self._price_per_night

    def set_price_per_night(self, price):
        """Sets the price per night for the room."""
        self._price_per_night = price

    def get_amenities(self):
        """Returns the list of amenities available in the room."""
        return self._amenities

    def set_amenities(self, amenities):
        """Sets the list of amenities available in the room."""
        self._amenities = amenities

    def get_is_available(self):
        """Returns the availability status of the room."""
        return self._is_available

    def set_is_available(self, is_available):
        """Sets the availability status of the room."""
        self._is_available = is_available

    def update_availability(self, status):
        """Updates the room's availability status."""
        self._is_available = status

    def __str__(self):
        return f"Room {self._room_number}: ${self._price_per_night}/night, Available: {self._is_available}"

class SingleRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, 100, ["WiFi", "TV", "Air Conditioning"])

class DoubleRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, 150, ["WiFi", "TV", "Mini Fridge", "Air Conditioning"])

class Suite(Room):
    def __init__(self, room_number):
        super().__init__(room_number, 300, ["WiFi", "TV", "Mini Fridge", "Jacuzzi", "Living Area"])

class Booking:
    """
    Represents a hotel room booking.
    """
    def __init__(self, guest, room, check_in_date, check_out_date, booking_id):
        """
        Initializes a new booking.
        :param guest: Guest object, the guest making the booking
        :param room: Room object, the room being booked
        :param check_in_date: str, check-in date
        :param check_out_date: str, check-out date
        :param booking_id: str, unique booking identifier
        """
        self._guest = guest
        self._room = room
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._booking_id = booking_id
        self._payment = None
        self._invoice = None

    def get_guest(self):
        """Returns the guest associated with the booking."""
        return self._guest

    def get_room(self):
        """Returns the room associated with the booking."""
        return self._room

    def get_check_in_date(self):
        """Returns the check-in date."""
        return self._check_in_date

    def get_check_out_date(self):
        """Returns the check-out date."""
        return self._check_out_date

    def get_booking_id(self):
        """Returns the booking ID."""
        return self._booking_id

    def set_payment(self, payment):
        """Assigns a payment method to the booking."""
        self._payment = payment

    def generate_invoice(self):
        """Generates an invoice for the booking."""
        nights = (self._check_out_date - self._check_in_date).days
        total = nights * self._room.get_price_per_night()
        self._invoice = {"total": total, "payment_method": self._payment}
        return self._invoice

    def __str__(self):
        return f"Booking ID: {self._booking_id}, {self._room} from {self._check_in_date} to {self._check_out_date}"

class ServiceRequest:
    """
    Represents a service request made by a hotel guest.
    """
    def __init__(self, request_type, details, status="Pending", request_date=None):
        self._request_type = request_type
        self._details = details
        self._status = status
        self._request_date = request_date or date.today()

    def __str__(self):
        return f"{self._request_type}: {self._details} ({self._status}), Date: {self._request_date}"

class Feedback:
    """
    Represents guest feedback for hotel services.
    """
    def __init__(self, rating, comments, guest_name, feedback_date):
        self._rating = rating
        self._comments = comments
        self._guest_name = guest_name
        self._feedback_date = feedback_date

    def __str__(self):
        return f"Feedback by {self._guest_name} on {self._feedback_date}: {self._rating}/5 - {self._comments}"






cli.py
from datetime import date, datetime
from abc import ABC, abstractmethod
import uuid

class Room:
    """
    Represents a hotel room with attributes such as price, amenities, and availability.
    """
    def __init__(self, room_number, price_per_night, amenities, is_available=True):
        self._room_number = room_number
        self._price_per_night = price_per_night
        self._amenities = amenities
        self._is_available = is_available

    def get_room_number(self):
        return self._room_number

    def get_price_per_night(self):
        return self._price_per_night

    def set_price_per_night(self, price):
        self._price_per_night = price

    def get_amenities(self):
        return self._amenities

    def set_amenities(self, amenities):
        self._amenities = amenities

    def get_is_available(self):
        return self._is_available

    def set_is_available(self, is_available):
        self._is_available = is_available

    def update_availability(self, status):
        self._is_available = status

    def __str__(self):
        return f"Room {self._room_number}: ${self._price_per_night}/night, Available: {self._is_available}"

class SingleRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, 100, ["WiFi", "TV", "Air Conditioning"])

class DoubleRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, 150, ["WiFi", "TV", "Mini Fridge", "Air Conditioning"])

class Suite(Room):
    def __init__(self, room_number):
        super().__init__(room_number, 300, ["WiFi", "TV", "Mini Fridge", "Jacuzzi", "Living Area"])

class Booking:
    """
    Represents a hotel room booking.
    """
    def __init__(self, guest, room, check_in_date, check_out_date, booking_id):
        self._guest = guest
        self._room = room
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._booking_id = booking_id
        self._payment = None
        self._invoice = None

    def get_guest(self):
        return self._guest

    def get_room(self):
        return self._room

    def get_check_in_date(self):
        return self._check_in_date

    def get_check_out_date(self):
        return self._check_out_date

    def get_booking_id(self):
        return self._booking_id

    def set_payment(self, payment):
        self._payment = payment

    def generate_invoice(self):
        nights = (self._check_out_date - self._check_in_date).days
        total = nights * self._room.get_price_per_night()
        self._invoice = {"total": total, "payment_method": self._payment}
        return self._invoice

    def __str__(self):
        return f"Booking ID: {self._booking_id}, {self._room} from {self._check_in_date} to {self._check_out_date}"

class ServiceRequest:
    """
    Represents a service request made by a hotel guest.
    """
    def __init__(self, request_type, details, status="Pending", request_date=None):
        self._request_type = request_type
        self._details = details
        self._status = status
        self._request_date = request_date or date.today()

    def __str__(self):
        return f"{self._request_type}: {self._details} ({self._status}), Date: {self._request_date}"

class Feedback:
    """
    Represents guest feedback for hotel services.
    """
    def __init__(self, rating, comments, guest_name, feedback_date):
        self._rating = rating
        self._comments = comments
        self._guest_name = guest_name
        self._feedback_date = feedback_date

    def __str__(self):
        return f"Feedback by {self._guest_name} on {self._feedback_date}: {self._rating}/5 - {self._comments}"

class Payment(ABC):
    """
    Abstract base class for different payment methods.
    """
    def __init__(self, amount, payment_date, transaction_id):
        self._amount = amount
        self._payment_date = payment_date
        self._transaction_id = transaction_id

    @abstractmethod
    def process_payment(self):
        pass

    def __str__(self):
        return f"Payment of ${self._amount} on {self._payment_date}, Transaction ID: {self._transaction_id}"

class CreditCardPayment(Payment):
    """
    Handles credit card payment processing.
    """
    def __init__(self, amount, card_number, expiry_date, payment_date, transaction_id):
        super().__init__(amount, payment_date, transaction_id)
        self._card_number = card_number
        self._expiry_date = expiry_date

    def process_payment(self):
        return f"Paid ${self._amount} via Credit Card on {self._payment_date}"

class MobileWalletPayment(Payment):
    """
    Handles mobile wallet payment processing.
    """
    def __init__(self, amount, wallet_type, phone_number, payment_date, transaction_id):
        super().__init__(amount, payment_date, transaction_id)
        self._wallet_type = wallet_type
        self._phone_number = phone_number

    def process_payment(self):
        return f"Paid ${self._amount} via {self._wallet_type} on {self._payment_date}"

class HotelCLI:
    """
    Command Line Interface (CLI) for the hotel management system.
    """
    def __init__(self):
        self.rooms = [SingleRoom(101), DoubleRoom(201), Suite(301)]

    def start(self):
        while True:
            print("\n=== Hotel Management System ===")
            print("1. Search Available Rooms")
            print("2. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                self.search_rooms()
            elif choice == '2':
                break

    def search_rooms(self):
        for room in self.rooms:
            if room.get_is_available():
                print(room)

if __name__ == "__main__":
    cli = HotelCLI()
    cli.start()
