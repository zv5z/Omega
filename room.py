class Room:
    """
    Abstract base class for hotel rooms.
    """
    def __init__(self, room_number, price_per_night, amenities, is_available=True):
        """
        Initialize a room.
        :param room_number: int, unique room number
        :param price_per_night: float, price per night for the room
        :param amenities: list, available amenities in the room
        :param is_available: bool, room availability status
        """
        self._room_number = room_number
        self._price_per_night = price_per_night
        self._amenities = amenities
        self._is_available = is_available

    @property
    def room_number(self):
        return self._room_number

    @property
    def price_per_night(self):
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        self._price_per_night = value

    @property
    def amenities(self):
        return self._amenities

    @amenities.setter
    def amenities(self, value):
        self._amenities = value

    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, value):
        self._is_available = value

    def update_availability(self, status):
        """
        Update the room availability status.
        """
        self._is_available = status

    def __str__(self):
        """
        String representation of the room.
        """
        return f"Room {self._room_number} - ${self._price_per_night}/night, Available: {self._is_available}"
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
        Initialize a new booking.
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

    @property
    def guest(self):
        return self._guest

    @property
    def room(self):
        return self._room

    @property
    def check_in_date(self):
        return self._check_in_date

    @property
    def check_out_date(self):
        return self._check_out_date

    @property
    def booking_id(self):
        return self._booking_id

    
    def set_payment(self, payment):
        """
        Assign a payment method to the booking.
        """
        self._payment = payment

    def generate_invoice(self):
        """
        Generate an invoice for the booking.
        """
        nights = (self._check_out_date - self._check_in_date).days
        total = nights * self._room.price_per_night
        self._invoice = {"total": total, "payment_method": self._payment}
        return self._invoice

    def __str__(self):
        """
        String representation of the booking.
        """
        return f"Booking ID: {self._booking_id}, {self._room} from {self._check_in_date} to {self._check_out_date}"
