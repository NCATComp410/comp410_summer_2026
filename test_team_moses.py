"""Unit test file for team moses"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_moses(unittest.TestCase):
    """Test team moses PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_ip_address(self):
        """Test IP_ADDRESS functionality"""

    def test_it_driver_license(self):
        """Test IT_DRIVER_LICENSE functionality"""

    def test_it_fiscal_code(self):
        """Test IT_FISCAL_CODE functionality"""

    def test_it_identity_card(self):
        """Test IT_IDENTITY_CARD functionality"""

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
