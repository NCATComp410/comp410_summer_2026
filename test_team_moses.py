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
        valid_codes = [
            "VRNGNY07D68C351V",
            "RCCMNL83S18D969H",
            "MRNMIA02E45L219X",
        ]

        for code in valid_codes:
            with self.subTest(code=code):
                text = f"Codice fiscale: {code}"
                results = analyze_text(text, ["IT_FISCAL_CODE"])

                self.assertEqual(len(results), 1)
                self.assertEqual(results[0].entity_type, "IT_FISCAL_CODE")
                self.assertEqual(text[results[0].start:results[0].end], code)
                self.assertGreater(results[0].score, 0)

        invalid_codes = [
            "1234567890123456",
            "ABCDEFGHIJKLMNO",
            "ABC123456789XYZ",
            "VRNGNY07D68C351K",
        ]

        for code in invalid_codes:
            with self.subTest(code=code):
                results = analyze_text(
                    f"Codice fiscale: {code}",
                    ["IT_FISCAL_CODE"],
                )
                self.assertEqual(results, [])

    def test_it_identity_card(self):
        """Test IT_IDENTITY_CARD functionality"""

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
