# CS50P : College Event Registration Project with python

## Author

- Name: [Mahesh Babu Sammeta](https://github.com/sammetamaheshbabu)
- GitHut : https://github.com/sammetamaheshbabu
- EDX Profile : https://profile.edx.org/u/sammetamaheshbabu
- I'm from Hyderabad, India.
- Date : 29-02-2024

## Table of Contents

1. [Introduction](#introduction)
2. [Objective](#objective)
3. [Features](#features)
4. [Project Overview](#project-overview)
5. [Working of the Project](#working-of-the-project)
6. [Libraries Used](#libraries-used)
7. [Installation and Usage](#installation-and-usage)
8. [Results](#results)
9. [Final Outcome](#final-outcome)
10. [Advantages](#advantages)
11. [Conclusion](#conclusion)
12. [Note](#note)
13. [Contact](#contact)

---

## DEMO Video link:

- ### [YouTube](www.youtube.com).

- ### [LinkedIn](http://www.LinkedIn.com).

## Introduction

The College Event Registration Project with Python is designed to facilitate event registration for students at MBU (Mohan Babu University). This project provides the Command line interface (CLI) for students to register for various events organized by the college. The system ensures smooth registration, validates user inputs, generates event passes (in the form of QR code), and creates event MBU Event Uniform with logo.

## Objective

The main objective of this project is to streamline the event registration process for MBU students. By automating the registration process, the project aims to:

- Simplify event registration procedures
- Reduce manual effort and paperwork
- Enhance the overall efficiency of event management

## Features

1. **Interactive Command-Line Interface (CLI)**: The project offers a user-friendly CLI for seamless interaction, allowing students to easily navigate through event options and registration steps.

2. **QR Code Event Pass Generation**: Upon successful registration, the system generates personalized event passes with QR codes, enabling quick and efficient entry to the chosen events.

3. **Automated Validation of User Inputs**: The project includes automated validation mechanisms to ensure that user-provided information is accurate and meets specified criteria, enhancing data integrity.

4. **PDF Generation for Event Passes and Uniforms**: Utilizing the FPDF library, the project dynamically generates PDF documents containing event passes and unique event uniforms with logos, providing tangible proofs of registration.

5. **Unit Testing with Pytest**: By incorporating unit tests using Pytest, the project ensures the reliability and correctness of its functionalities, contributing to its robustness and stability.

## Project Overview

The project consists of two Python scripts: `project.py` and `test_project.py`.

### `project.py`

This script contains the main functionality of the project, including event details display, event selection, registration form filling, event pass generation, and creates unique event MBU Event Uniform with logo.

### `test_project.py`

This script contains unit tests for the functions defined in `project.py`. It ensures the correctness of the project's functionalities through automated testing.

## Working Of The Project

The project follows a sequential workflow as outlined below:

1. **Event Details Display**: The program displays a list of available events for registration.
2. **Event Selection**: Users select an event by entering the corresponding event number.
3. **Registration Form**: Users fill out the registration form with their details such as name, ID, email, phone number, year, and branch.
4. **Event Pass Generation**: Upon successful registration, the system generates an event pass in PDF format containing QR code the user's details and event information.
5. **Event Uniform With Logo** : Additionally, the program generates an creates unique event MBU Event Uniform with logo in PDF format with the user's name, ID, and event details.

## Libraries Used

The project utilizes the following Python libraries:

- `pyfiglet`: For ASCII art text formatting.
- `emoji`: For adding emojis to the console output.
- `qrcode`: For generating QR codes for event passes.
- `re`: For regular expression-based validation of email addresses.
- `FPDF2`: For creating PDF documents.
- `pytest`: For unit testing.

## Installation And Usage

### Installation

1. Clone the repository:

```bash
$ https://github.com/sammetamaheshbabu/College-Event-Registration-Project-with-python-CS50P.git
```

2. Navigate to the project directory:

```bash
$ cd College-Event-Registration-Project-with-python-CS50P
```

3. To install the required dependencies, use the following command:

```bash
pip install -r requirements.txt
```

### Usage

1. Run the `project.py` script using Python:

```bash
python project.py
```

2. Follow the on-screen instructions to select an event and fill out the registration form.

3. Upon successful registration, event passes and event details certificates will be generated.

### Testing

Unit tests for the project functions are provided in the `test_project.py` script. To run the tests, use the following command:

```bash
pytest test_project.py
```

## Installation

To install the required dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the `project.py` script using Python:

```bash
python project.py
```

2. Follow the on-screen instructions to select an event and fill out the registration form.

3. Upon successful registration, event passes and event details certificates will be generated.

## Testing

Unit tests for the project functions are provided in the `test_project.py` script. To run the tests, use the following command:

```bash
pytest test_project.py
```

## Results

### 1. QR Code Event Pass ( PDF)

[PDF with mobile number as file name](9160842635.pdf)

- [QR Code Scanner Website](https://scanqr.org/#scan)

### 2. Event Uniform preview With Logo ( PDF)

[PDF with ID as file name ](21125A1212.pdf)

## Final Outcome

The final outcome of the project includes:

- Simplified event registration process.
- Generation of event passes and creates unique event MBU Event Uniform with logo in PDF format.
- Automated validation of user inputs for correctness.
- Enhanced user experience through interactive console interface.

## Advantages

The Python College Event Registration Project offers several advantages:

- **Efficiency**: Automates the event registration process, saving time for both students and event organizers.
- **Accuracy**: Ensures accurate capture and validation of user data.
- **User-Friendly**: Provides a simple the Command line interface (CLI).
- **Scalability**: Easily extendable to accommodate future enhancements and features.

## Conclusion

The Python College Event Registration Project effectively addresses the challenges associated with event registration at MBU. By leveraging Python programming and various libraries, the project offers a robust solution for managing college events efficiently. With its user-centric design and seamless workflow, the project contributes to enhancing the overall experience of students participating in college events.

## This was CS50P! 😊

I especially want to give my thanks to our instructor, [David J. Malan](https://www.linkedin.com/in/malan/).

## Note :

This project is solely focused on Python. It is part of my CS50's Introduction to Programming with Python course. We do not involve any databases or web interfaces. It is a CLI (Command-Line Interface). Further implementation includes trying to collect a database and implementing it in a web interface for the next version of this project.

## Contact

For any inquiries or support, please contact [Linkedin](https://www.linkedin.com/in/sammetamaheshbabu/) ,[Instagram](https://www.instagram.com/sammetamaheshbabu/).

---
