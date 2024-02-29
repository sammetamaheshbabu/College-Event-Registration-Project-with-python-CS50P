import pyfiglet  # Library for creating ASCII art text
import emoji  # Library for working with emojis
import qrcode  # Library for generating QR codes
import re  # Regular expression library for string matching
from fpdf import FPDF  # Library for creating PDF files

# Dictionary containing event IDs and their corresponding names
EVENTS = {
    "1": "Sports",
    "2": "Cultural Activities",
    "3": "Presentations",
    "4": "Workshops",
    "5": "Hackathons",
}

# List of acceptable branches
ACCEPTABLE_BRANCHES = ["CSE", "IT", "CSSE", "AI", "ML", "MEC", "CIVIL", "EEE", "ECE"]


# Function to display event details
def event_details():
    """
    Displays event details including event names and IDs.
    """
    title = pyfiglet.figlet_format("MBU", font="doh")
    print(title, end="")
    print("Event Registration Portal")
    print("================================")
    # Print the list of events
    print("List of Events:")
    for event_id, event_name in EVENTS.items():
        print(f"{event_id}. {event_name}")


# Function to select an event
def select_event():
    """
    Allows the user to select an event by entering its number.
    Returns the event ID and name.
    """
    while True:
        event_id = input("Select an event by entering its number: ")
        event_name = EVENTS.get(event_id)
        if event_name:
            print("You have selected:", event_name)
            return event_id, event_name
        else:
            print("Invalid event number. Please select a valid event.")


# Function to gather registration information
def registration_form(event_id, event_name):
    """
    Gathers registration information from the user.
    Returns student details including ID, name, phone, email, year, and branch.
    """
    print("Registration Form")
    print("==================")

    # Gather student name
    while True:
        student_name = input("Enter your name: ")
        if len(student_name) > 15:
            print("Error: Name must be 15 characters or fewer. Please try again.")
        else:
            break

    # Gather student ID
    while True:
        student_id = input("Enter your ID: ")
        if len(student_id) > 10:
            print("Error: Student ID must be 10 characters or fewer. Please try again.")
        else:
            break

    # Gather student email
    invalid_count = 0
    while True:
        student_email = input("Enter your email address: ")
        if re.search(r"^\w+@mbu\.asia$", student_email, re.IGNORECASE):
            break
        else:
            invalid_count += 1
            if invalid_count == 2:
                print(
                    "Please use your college provided email id. These events are conducted for MBU students only."
                )
            print("Invalid email address. Please try again.")

    # Gather student phone number
    invalid_count = 0
    while True:
        student_phone = input("Enter your phone number:+91 ")
        if student_phone.isdigit() and len(student_phone) == 10:
            break
        else:
            invalid_count += 1
            if invalid_count == 2:
                print(
                    "Please use your indian mobile number as per collage data. These events are conducted for MBU students only."
                )
            print("Invalid phone number. Please enter 10 digits.")

    # Gather student year
    while True:
        student_year = input("Enter your year (1st to 4th year): ")
        if student_year not in ["1", "2", "3", "4"]:
            print("Invalid year. Please enter a year from 1st to 4th.")
        else:
            break

    # Gather student branch
    while True:
        student_branch = input("Enter your branch: ").upper()
        acceptable_branches = [
            "CSE",
            "IT",
            "CSSE",
            "AI",
            "ML",
            "MEC",
            "CIVIL",
            "EEE",
            "ECE",
        ]
        if student_branch not in acceptable_branches:
            print("Invalid branch. Please enter a valid branch.")
        else:
            break

    print(emoji.emojize("Registration successful!:thumbs_up:"))
    return (
        student_id,
        student_name,
        student_phone,
        student_email,
        student_year,
        student_branch,
    )


# Function to print event details in a PDF
def print_event_details(event_name, student_id, student_name):
    """
    Prints event details along with student information in a PDF.
    """

    class PDF(FPDF):
        def header(self):
            self.image(".\\shirtificate.png", 10, 70, 190)
            self.set_font("helvetica", "", 48)
            self.cell(0, 57, "MBU Event Uniform", align="C")
            self.ln(160)

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=32)
    pdf.set_text_color(255, 255, 255)

    # Adding event details
    pdf.image("main-logo.png", x=65, y=120, w=70)
    pdf.cell(0, 20, f"{event_name}", align="C", ln=True)

    # Adding student details
    pdf.cell(0, 20, f"{student_name}", align="C", ln=True)
    pdf.cell(0, 20, f" {student_id}", align="C", ln=True)

    pdf_name = f"{student_id}.pdf"
    pdf.output(pdf_name)

    print(f"PDF generated successfully as {pdf_name}")


# Function to generate event pass
def event_pass(student_id, student_name, student_phone, student_email, event_name):
    """
    Generates an event pass in the form of a PDF containing QR code.
    """
    try:
        pdf = FPDF()
        pdf.add_page(format=(250, 250))
        img = qrcode.make(
            f"Student Name:{student_name},\nStudent ID:{student_id},\nStudent Phone:{student_phone},\nStudent Email:{student_email},\nEvent Name:{event_name}"
        )
        pdf.image(img.get_image(), x=0, y=0)
        # Saving PDF with student's phone number as filename
        pdf_name = f"{student_phone}.pdf"
        pdf.output(pdf_name)

        print(f"Event pass generated successfully as {pdf_name}")
    except Exception as e:
        print(f"An error occurred while generating event pass: {str(e)}")


# Main function to execute the program
def main():
    """
    Main function to execute the event registration process.
    """
    event_details()
    event_id, event_name = select_event()
    registration_details = registration_form(event_id, event_name)
    student_id, student_name, student_phone, student_email, _, _ = registration_details
    print_event_details(event_name, student_id, student_name)
    event_pass(student_id, student_name, student_phone, student_email, event_name)


if __name__ == "__main__":
    main()
