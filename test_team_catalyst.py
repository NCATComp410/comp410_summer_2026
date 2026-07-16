"""Unit test file for team catalyst"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_catalyst(unittest.TestCase):
    """Test team catalyst PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_credit_card(self):
        """Test CREDIT_CARD functionality"""

    def test_crypto(self):
        """Test CRYPTO functionality"""

    def test_date_time(self):
        """Test DATE_TIME functionality"""

    def test_email_address(self):
        """Test EMAIL_ADDRESS functionality"""

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""
        # positive test case
        test_str = "My DEA certificate number is AB1234563"
        result = analyze_text(test_str, ["MEDICAL_LICENSE"])
        self.assertEqual(result[0].entity_type, "MEDICAL_LICENSE")

        # negative test case
        test_str = "My DEA certificate number is AB1234567"
        result = analyze_text(test_str, ["MEDICAL_LICENSE"])
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
