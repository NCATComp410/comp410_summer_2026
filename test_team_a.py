"""Unit test file for team a"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_a(unittest.TestCase):
    """Test team a PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""

    def test_url(self):
        """Test URL functionality"""

    def test_us_bank_number(self):
        """Test US_BANK_NUMBER functionality"""

    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""
        # Positive test
        text = "My driver's license number is A1234567"
        results = analyze_text(text, entity_list=["US_DRIVER_LICENSE"])

        self.assertTrue(
            any(result.entity_type == "US_DRIVER_LICENSE" for result in results),
            msg=f"Expected US_DRIVER_LICENSE to be detected in: {text}"
        )

        # Negative test
        text = "Hello, my name is John Smith."
        results = analyze_text(text, entity_list=["US_DRIVER_LICENSE"])

        self.assertFalse(
            any(result.entity_type == "US_DRIVER_LICENSE" for result in results),
            msg=f"Did not expect US_DRIVER_LICENSE to be detected in: {text}"
        )

    def test_us_itin(self):
        """Test US_ITIN functionality"""

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
