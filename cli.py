from datetime import datetime
from hotel.guest import Guest
from hotel.room import SingleRoom, DoubleRoom, Suite
from hotel.booking import Booking, CreditCardPayment, MobileWalletPayment
from hotel.services import ServiceRequest, Feedback
import uuid

class HotelCLI:
    """
    Command Line Interface (CLI) for the hotel management system.
    """
    def __init__(self):
        """
        Initialize the hotel CLI with available rooms and guest list.
        """
        self.guests = []
        self.rooms = [
            SingleRoom(101),
            DoubleRoom(201),
            Suite(301)
        ]
        self.current_guest = None

    def start(self):
        """
        Start the CLI application, displaying the main menu.
        """
        while True:
            print("\n=== Royal Stay Hotel Management System ===")
            print("1. Create Guest Account")
            print("2. Search Available Rooms")
            print("3. Make Booking")
            print("4. View Reservation History")
            print("5. Request Service")
            print("6. Submit Feedback")
            print("7. Exit")
            
            choice = input("Enter your choice (1-7): ")
            
            if choice == '1':
                self.create_guest_account()
            elif choice == '2':
                self.search_rooms()
            elif choice == '3':
                self.make_booking()
            elif choice == '4':
                self.view_reservation_history()
            elif choice == '5':
                self.request_service()
            elif choice == '6':
                self.submit_feedback()
            elif choice == '7':
                print("Thank you for using Royal Stay Hotel System!")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_guest_account(self):
        """
        Create a new guest account by collecting user details.
        """
        guest_id = str(uuid.uuid4())[:8]  # Generate unique guest ID
        name = input("Enter your full name: ")
        email = input("Enter your email: ")
        contact = input("Enter your contact number: ")
        new_guest = Guest(guest_id, name, email, contact)
        self.guests.append(new_guest)
        self.current_guest = new_guest
        print(f"\nAccount created successfully! Welcome, {name}! Your Guest ID: {guest_id}")
    
    def search_rooms(self):
        """
        Display available rooms and their details.
        """
        print("\nAvailable Rooms:")
        for room in self.rooms:
            if room.is_available:
                print(f"{room.__class__.__name__} Room {room.room_number} - ${room.price_per_night}/night")
                print(f"Amenities: {', '.join(room.amenities)}")
                print("-" * 40)
    def view_reservation_history(self):
        """
        Display the current guest's booking history.
        """
        if not self.current_guest:
            print("Please create an account or login first!")
            return

        history = self.current_guest.view_reservation_history()
        if not history:
            print("You have no previous reservations.")
        else:
            print("\n=== Your Reservation History ===")
            for booking in history:
                print(booking)
                print("-" * 40)


    def make_booking(self):
        """
        Allow a guest to book a room by selecting available options.
        """
        if not self.current_guest:
            print("Please create an account or login first!")
            return

        try:
            room_number = int(input("Enter room number to book: "))
            selected_room = next((r for r in self.rooms if r.room_number == room_number), None)
            
            if not selected_room or not selected_room.is_available:
                print("Invalid room number or room not available")
                return

            check_in = datetime.strptime(input("Enter check-in date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            check_out = datetime.strptime(input("Enter check-out date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            
            if check_out <= check_in:
                print("Check-out date must be after check-in date")
                return
            
            booking_id = str(uuid.uuid4())[:8]  # Generate unique booking ID
            booking = Booking(self.current_guest, selected_room, check_in, check_out, booking_id)
            
            # Choose payment method
            print("\nPayment Options:")
            print("1. Credit Card")
            print("2. Mobile Wallet")
            pay_choice = input("Select payment method (1-2): ")
            
            amount = selected_room.price_per_night * (check_out - check_in).days
            payment_date = str(datetime.today().date())
            transaction_id = str(uuid.uuid4())[:8]
            
            if pay_choice == '1':
                card = input("Enter card number: ")
                expiry = input("Enter expiry (MM/YY): ")
                payment = CreditCardPayment(amount, card, expiry, payment_date, transaction_id)
            elif pay_choice == '2':
                wallet = input("Enter wallet type (e.g., PayPal, Google Pay): ")
                number = input("Enter mobile number: ")
                payment = MobileWalletPayment(amount, wallet, number, payment_date, transaction_id)
            else:
                print("Invalid payment choice")
                return

            # Process booking and payment
            booking.set_payment(payment)
            invoice = booking.generate_invoice()
            selected_room.update_availability(False)
            self.current_guest.make_booking(booking)
            
            # Display booking confirmation
            print("\nBooking Successful!")
            print(f"Invoice Total: ${invoice['total']}")
            print(payment.process_payment())

        except ValueError as e:
            print(f"Error: {str(e)}")
    
    def request_service(self):
        """
        Allows a guest to request a hotel service.
        """
        if not self.current_guest:
            print("Please create an account or login first!")
            return

        print("\n=== Service Request ===")
        request_type = input("Enter service type (e.g., Housekeeping, Room Service): ")
        details = input("Enter request details: ")

        service_request = ServiceRequest(request_type, details)
        print("\nService request submitted successfully!")
        print(service_request)
    
    def submit_feedback(self):
        """
        Allows a guest to submit feedback.
        """
        if not self.current_guest:
            print("Please create an account or login first!")
            return

        print("\n=== Submit Feedback ===")
        rating = int(input("Enter your rating (1-5): "))
        comments = input("Enter your feedback comments: ")

        feedback = Feedback(rating, comments, self.current_guest.name, str(datetime.today().date()))
        print("\nThank you for your feedback!")
        print(feedback)

if __name__ == "__main__":
    cli = HotelCLI()
    cli.start()