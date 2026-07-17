"""Unit test file for team null"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_null(unittest.TestCase):
    """Test team null PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_us_ssn(self):
        """Test US_SSN functionality"""
        # positive test case
        test_str = 'my SSN is 111-22-1234'
        result = analyze_text(test_str, ['US_SSN'])
        self.assertEqual(result[0].entity_type, 'US_SSN')

        # negative test case
        test_str = 'my SSN is 123456789'
        result = analyze_text(test_str, ['US_SSN'])
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
