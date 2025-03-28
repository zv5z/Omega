from datetime import date
class ServiceRequest:
    """
    Represents a service request made by a hotel guest.
    """
    def __init__(self, request_type, details, status="Pending", request_date=None):
        """
        Initialize a service request.
        :param request_type: str, type of service requested (e.g., Housekeeping, Room Service)
        :param details: str, additional details about the request
        :param status: str, current status of the request (default: Pending)
        :param request_date: str, date of request submission
        """
        self._request_type = request_type
        self._details = details
        self._status = status
        self._request_date = request_date

    @property
    def request_type(self):
        return self._request_type

    @request_type.setter
    def request_type(self, value):
        self._request_type = value

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        self._details = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def request_date(self):
        return self._request_date

    @request_date.setter
    def request_date(self, value):
        self._request_date = value

    def __str__(self):
        """
        String representation of the service request.
        """
        return f"{self._request_type}: {self._details} ({self._status}), Date: {self._request_date}"


class Feedback:
    """
    Represents guest feedback for hotel services.
    """
    def __init__(self, rating, comments, guest_name, feedback_date):
        """
        Initialize a feedback entry.
        :param rating: int, rating out of 5
        :param comments: str, additional feedback comments
        :param guest_name: str, name of the guest providing feedback
        :param feedback_date: str, date feedback was given
        """
        self._rating = rating
        self._comments = comments
        self._guest_name = guest_name
        self._feedback_date = feedback_date

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value

    @property
    def comments(self):
        return self._comments

    @comments.setter
    def comments(self, value):
        self._comments = value

    @property
    def guest_name(self):
        return self._guest_name

    @guest_name.setter
    def guest_name(self, value):
        self._guest_name = value

    @property
    def feedback_date(self):
        return self._feedback_date

    @feedback_date.setter
    def feedback_date(self, value):
        self._feedback_date = value

    def __str__(self):
        """
        String representation of the feedback.
        """
        return f"Feedback by {self._guest_name} on {self._feedback_date}: {self._rating}/5 - {self._comments}"
