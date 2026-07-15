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

    # positive test case
        my_bank = "12345678901234567"
        result = analyze_text(my_bank, ["US_BANK_NUMBER"])
        print(result)
        self.assertEqual(result[0].entity_type, "US_BANK_NUMBER")

    # negative test case
        my_bank= "1234567"
        result = analyze_text(my_bank, ["US_BANK_NUMBER"])
        print(result)
        self.assertFalse(result)


    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""

    def test_us_itin(self):
        """Test US_ITIN functionality"""

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
