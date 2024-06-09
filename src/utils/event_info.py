#event details as variables
EVENT_NAME = "Tech Innovation Conference 2024"
EVENT_DATE = "June 25, 2024"
EVENT_TIME = "9:00 AM to 5:00 PM"
EVENT_LOCATION = "Grand Hall, City Convention Center"
EVENT_DESCRIPTION = (
    "Join us for a day of inspiring talks and networking with leading professionals in the tech industry. "
    "Learn about the latest trends in technology and innovation."
)
REGISTRATION_INFO = "To register, use the /register command."
CONTACT_INFO = "For more details or assistance, feel free to reach out to our support team."

# send start message
def event_infor_message():
    message = (
        f"Hello and welcome to the Event Bot! 🎉\n\n"
        f"We're excited to have you here.\n\n"
        f"<b>Upcoming Event Details</b>:\n"
        f"<b>Event Name</b>: {EVENT_NAME}\n"
        f"<b>Date and Time</b>: {EVENT_DATE}, {EVENT_TIME}\n"
        f"<b>Location</b>: {EVENT_LOCATION}\n\n"
        f"<b>Description</b>:\n"
        f"{EVENT_DESCRIPTION}\n\n"
        f"<b>Registration</b>:\n"
        f"{REGISTRATION_INFO}\n\n"
        f"{CONTACT_INFO}\n\n"
        "We look forward to seeing you there! 🚀"
        ) 
    return message

def ticket_info_message(ticket_id, event_name, event_date, created_time,email):
    message = (
        f"<b>Ticket Details</b>:\n\n"
        f"<b>Ticket ID</b>: {ticket_id}\n"
        f"<b>Email</b>: {email}\n"
        f"<b>Event Name</b>: {event_name}\n"
        f"<b>Event Date</b>: {event_date}\n"
        f"<b>Created Time</b>: {created_time}\n\n"
        "We look forward to seeing you at the event! 🚀"
    )
    return message
    

def help_info_message():
    help_message = (
        "Welcome to the Event Ticketing Bot! 🎟️\n\n"
        "To start registering for tickets, use the /register command.\n\n"
        "Steps to follow:\n"
        "1. Provide your name when prompted.\n"
        "2. Enter a valid email address.\n"
        "3. Specify the number of tickets you want (between 1-5).\n\n"
        "After completing these steps, the system will provide you with your ticket details.\n"
        "Finally, you will be added to the Event Group.\n"
        "To cancel the registration process at any point, use the /cancel command.\n\n"
    )
    return help_message