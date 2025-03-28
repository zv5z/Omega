class LoyaltyAccount:
    """
    Represents a guest's loyalty account for earning and redeeming points.
    """
    def __init__(self, account_id, points=0, tier='Basic', last_updated=None):
        """
        Initialize a loyalty account.
        :param account_id: str, unique identifier for the loyalty account
        :param points: int, current loyalty points
        :param tier: str, membership tier (e.g., Basic, Silver, Gold)
        :param last_updated: str, last date points were updated
        """
        self._account_id = account_id
        self._points = points
        self._tier = tier
        self._last_updated = last_updated

    @property
    def account_id(self):
        return self._account_id

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    @property
    def tier(self):
        return self._tier

    @tier.setter
    def tier(self, value):
        self._tier = value

    @property
    def last_updated(self):
        return self._last_updated

    @last_updated.setter
    def last_updated(self, value):
        self._last_updated = value

    def earn_points(self, amount):
        """
        Add points to the account.
        """
        self._points += amount

    def redeem_points(self, amount):
        """
        Redeem points from the account.
        """
        if self._points >= amount:
            self._points -= amount
        else:
            raise ValueError("Insufficient points")

    def __str__(self):
        """
        String representation of the loyalty account.
        """
        return f"Loyalty Account {self._account_id}: {self._points} points, Tier: {self._tier}"


class Guest:
    """
    Represents a hotel guest with personal details and booking history.
    """
    def __init__(self, guest_id, name, email, contact, loyalty_account=None):
        """
        Initialize a guest.
        :param guest_id: str, unique identifier for the guest
        :param name: str, guest's name
        :param email: str, guest's email address
        :param contact: str, guest's contact number
        :param loyalty_account: LoyaltyAccount object, guest's loyalty program details
        """
        self._guest_id = guest_id
        self._name = name
        self._email = email
        self._contact = contact
        self._loyalty_account = loyalty_account if loyalty_account else LoyaltyAccount(guest_id)
        self._bookings = []

    @property
    def guest_id(self):
        return self._guest_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value

    @property
    def loyalty_account(self):
        return self._loyalty_account

    @property
    def bookings(self):
        return self._bookings

    def make_booking(self, booking):
        """
        Add a booking to the guest's history and earn loyalty points.
        """
        self._bookings.append(booking)
        self._loyalty_account.earn_points(100)  # Example: 100 points per booking

    def view_reservation_history(self):
        """
        Retrieve the guest's booking history.
        """
        return self._bookings

    def __str__(self):
        """
        String representation of the guest.
        """
        return f"Guest {self._guest_id}: {self._name}, Email: {self._email}, Contact: {self._contact}"