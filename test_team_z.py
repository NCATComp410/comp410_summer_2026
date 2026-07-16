"""Unit test file for team z"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_z(unittest.TestCase):
    """Test team z PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_phone_number(self):
        """Test PHONE_NUMBER functionality"""

    def test_location(self):
        """Test LOCATION functionality"""

    def test_person(self):
        """Test PERSON functionality"""

    def test_uk_nhs(self):
        """Test UK_NHS functionality"""

    def test_uk_nino(self):
        """Test UK_NINO functionality"""

    # Positive Test Case

        test_str = "The National Insurance number is AB123456C."
        result = analyze_text(test_str, ['UK_NINO'])
        self.assertEqual(result[0].entity_type, 'UK_NINO')

    # Negative Test Case (invalid format)

        test_str = "The National Insurance number is AB12345C."
        result = analyze_text(test_str, ['UK_NINO'])
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
