from abc import ABC, abstractmethod
from datetime import date

class Payment:
    """
    Abstract base class for different payment methods.
    """
    def __init__(self, amount, payment_date, transaction_id):
        """
        Initialize payment with an amount.
        :param amount: float, payment amount
        :param payment_date: str, date of payment transaction
        :param transaction_id: str, unique transaction identifier
        """
        self._amount = amount
        self._payment_date = payment_date
        self._transaction_id = transaction_id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, value):
        self._payment_date = value

    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value

    def __str__(self):
        """
        String representation of the payment.
        """
        return f"Payment of ${self._amount} on {self._payment_date}, Transaction ID: {self._transaction_id}"


class CreditCardPayment(Payment):
    """
    Handles credit card payment processing.
    """
    def __init__(self, amount, card_number, expiry_date, payment_date, transaction_id):
        """
        Initialize credit card payment.
        :param amount: float, payment amount
        :param card_number: str, credit card number
        :param expiry_date: str, card expiry date
        :param payment_date: str, date of payment
        :param transaction_id: str, unique transaction ID
        """
        super().__init__(amount, payment_date, transaction_id)
        self._card_number = card_number
        self._expiry_date = expiry_date

    @property
    def card_number(self):
        return self._card_number

    @property
    def expiry_date(self):
        return self._expiry_date

    def process_payment(self):
        """
        Process payment via credit card.
        :return: str, payment confirmation message
        """
        return f"Paid ${self._amount} via Credit Card on {self._payment_date}"


class MobileWalletPayment(Payment):
    """
    Handles mobile wallet payment processing.
    """
    def __init__(self, amount, wallet_type, phone_number, payment_date, transaction_id):
        """
        Initialize mobile wallet payment.
        :param amount: float, payment amount
        :param wallet_type: str, type of mobile wallet (e.g., PayPal)
        :param phone_number: str, mobile number linked to wallet
        :param payment_date: str, date of payment
        :param transaction_id: str, unique transaction ID
        """
        super().__init__(amount, payment_date, transaction_id)
        self._wallet_type = wallet_type
        self._phone_number = phone_number

    @property
    def wallet_type(self):
        return self._wallet_type

    @property
    def phone_number(self):
        return self._phone_number

    def process_payment(self):
        """
        Process payment via mobile wallet.
        :return: str, payment confirmation message
        """
        return f"Paid ${self._amount} via {self._wallet_type} on {self._payment_date}"

class Booking:
    """
    Represents a hotel room booking.
    """
    def __init__(self, guest, room, check_in_date, check_out_date, booking_id):
        """
        Initialize a new booking.
        :param guest: Guest object, the guest making the booking
        :param room: Room object, the room being booked
        :param check_in_date: date, check-in date
        :param check_out_date: date, check-out date
        :param booking_id: str, unique booking identifier
        """
        self._guest = guest
        self._room = room
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._booking_id = booking_id  # Store booking ID
        self._payment = None
        self._invoice = None

    @property
    def booking_id(self):
        return self._booking_id

    def set_payment(self, payment):
        """
        Assign a payment method to the booking.
        :param payment: Payment object
        """
        self._payment = payment

    def generate_invoice(self):
        """
        Generate an invoice for the booking.
        :return: dict, invoice details including total amount and payment method
        """
        nights = (self._check_out_date - self._check_in_date).days
        total = nights * self._room._price_per_night
        self._invoice = {"total": total, "payment_method": self._payment}
        return self._invoice

    def __str__(self):
        """
        String representation of the booking.
        :return: str, formatted booking details
        """
        return f"Booking: {self._room} from {self._check_in_date} to {self._check_out_date}"
