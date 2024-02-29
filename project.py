import pyfiglet
import emoji
import qrcode
import re
from fpdf import FPDF

EVENTS = {
    "1": "Sports",
    "2": "Cultural Activities",
    "3": "Presentations",
    "4": "Workshops",
    "5": "Hackathons"
}

ACCEPTABLE_BRANCHES = [
    "CSE", "IT", "CSSE", "AI", "ML",
    "MEC", "CIVIL", "EEE", "ECE"
]

def event_details():
    title = pyfiglet.figlet_format("MBU", font="doh")
    print(title , end="")
    print("Event Registration Portal")
    print("================================")
    # Print the list of events
    print("List of Events:")
    for event_id, event_name in EVENTS.items():
        print(f"{event_id}. {event_name}")

def select_event():
    while True:
        event_id = input("Select an event by entering its number: ")
        event_name = EVENTS.get(event_id)
        if event_name:
            print("You have selected:", event_name)
            return event_id, event_name
        else:
            print("Invalid event number. Please select a valid event.")

def registration_form(event_id, event_name):
    print("Registration Form")
    print("==================")
    
    while True:
        student_name = input("Enter your name: ")
        if len(student_name) > 15:
            print("Error: Name must be 15 characters or fewer. Please try again.")
        else:
            break

    while True:
        student_id = input("Enter your ID: ")
        if len(student_id) > 10:
            print("Error: Student ID must be 10 characters or fewer. Please try again.")
        else:
            break

    invalid_count = 0
    while True:
        student_email = input("Enter your email address: ")
        if re.search(r"^\w+@mbu\.asia$", student_email, re.IGNORECASE):
            break
        else:
            invalid_count += 1 
            if invalid_count == 2:
                print("Please use your college provided email id. These events are conducted for MBU students only.")
            print("Invalid email address. Please try again.")


    invalid_count =0
    while True:
        student_phone = input("Enter your phone number:+91 ")
        if student_phone.isdigit() and len(student_phone) == 10:
            break  
        else:
            invalid_count += 1 
            if invalid_count == 2:
                print("Please use your indian mobile number as per collage data. These events are conducted for MBU students only.")
            print("Invalid phone number. Please enter 10 digits.")


    while True:
        student_year = input("Enter your year (1st to 4th year): ")
        if student_year not in ["1", "2", "3", "4"]:
            print("Invalid year. Please enter a year from 1st to 4th.")
        else:
            break


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
    return student_id, student_name, student_phone, student_email, student_year, student_branch

def print_event_details(event_name, student_id, student_name):
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
    pdf.image("main-logo.png",x=65, y=120, w=70 )
    pdf.cell(0, 20, f"{event_name}",align="C", ln=True)

    # Adding student details
    pdf.cell(0, 20, f"{student_name}",align="C", ln=True)
    pdf.cell(0, 20, f" {student_id}",align="C", ln=True)

    pdf_name = f"{student_id}.pdf"
    pdf.output(pdf_name)

    print(f"PDF generated successfully as {pdf_name}")

def event_pass(student_id, student_name, student_phone, student_email, event_name):
    try:
        pdf = FPDF()
        pdf.add_page(format=(250, 250))
        img = qrcode.make(f"Student Name:{student_name},\nStudent ID:{student_id},\nStudent Phone:{student_phone},\nStudent Email:{student_email},\nEvent Name:{event_name}")
        pdf.image(img.get_image(), x=0, y=0)
        # Saving PDF with student's phone number as filename
        pdf_name = f"{student_phone}.pdf"
        pdf.output(pdf_name)

        print(f"Event pass generated successfully as {pdf_name}")
    except Exception as e:
        print(f"An error occurred while generating event pass: {str(e)}")

def main():
    event_details()
    event_id, event_name = select_event()
    registration_details = registration_form(event_id, event_name)
    student_id, student_name, student_phone, student_email, _, _ = registration_details
    print_event_details(event_name, student_id, student_name)
    event_pass(student_id, student_name, student_phone, student_email, event_name)

if __name__ == "__main__":
    main()
