import pytest
from unittest.mock import patch
import project
from project import event_details


class TestProjectFunctions:
    @patch("builtins.input", side_effect=["1"])
    def test_select_event(self, mock_input):
        # Test the select_event function to ensure correct event selection
        event_id, event_name = project.select_event()
        assert event_id == "1"
        assert event_name == "Sports"

    @patch(
        "builtins.input",
        side_effect=[
            "John Doe",
            "1234567890",
            "email@mbu.asia",
            "9876543210",
            "3",
            "CSE",
        ],
    )
    def test_registration_form(self, mock_input):
        # Test the registration_form function to ensure correct registration details
        registration_details = project.registration_form("1", "Sports")
        assert registration_details == (
            "1234567890",
            "John Doe",
            "9876543210",
            "email@mbu.asia",
            "3",
            "CSE",
        )

    @patch("project.FPDF")
    @patch("qrcode.make")
    def test_event_pass(self, mock_qrcode_make, mock_fpdf):
        # Test the event_pass function to ensure correct generation of event passes
        student_id = "1234567890"
        student_name = "John Doe"
        student_phone = "9876543210"
        student_email = "email@mbu.asia"
        event_name = "Sports"
        project.event_pass(
            student_id, student_name, student_phone, student_email, event_name
        )
        # Add assertions for PDF generation

    @patch("project.FPDF")
    def test_print_event_details(self, mock_fpdf):
        # Test the print_event_details function to ensure correct generation of event details PDF
        event_name = "Sports"
        student_id = "1234567890"
        student_name = "John Doe"
        project.print_event_details(event_name, student_id, student_name)
        # Add assertions for PDF generation


if __name__ == "__main__":
    pytest.main()
