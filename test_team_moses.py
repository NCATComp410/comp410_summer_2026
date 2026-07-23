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
        # positive test case
        test_str = "My IP address is 192.168.1.1"
        result = analyze_text(test_str, ["IP_ADDRESS"])
        self.assertTrue(result)
        self.assertEqual(result[0].entity_type, 'IP_ADDRESS')
        # negative test case
        test_str = "Hello, my name is John Smith"
        result = analyze_text(test_str, ["IP_ADDRESS"])
        self.assertFalse(result)

    def test_it_driver_license(self):
        """Test IT_DRIVER_LICENSE functionality"""
        test_str = "My Italian driver's license number is AB1234567C"
        result = analyze_text(test_str, ["IT_DRIVER_LICENSE"])
        self.assertEqual(result[0].entity_type, 'IT_DRIVER_LICENSE')

        test_str = "Hello, my name is John Smith"
        result = analyze_text(test_str, ["IT_DRIVER_LICENSE"])
        self.assertFalse(result)

    def test_it_fiscal_code(self):
        """Test IT_FISCAL_CODE functionality"""
        # positive test case
        test_str = 'my fiscal code is VRNGNY07D68C351V'
        result = analyze_text(test_str, ['IT_FISCAL_CODE'])
        self.assertEqual(result[0].entity_type, 'IT_FISCAL_CODE')

        # negative test case
        test_str = 'my fiscal code is 1234567890123456'
        result = analyze_text(test_str, ['IT_FISCAL_CODE'])
        self.assertFalse(result)

    def test_it_identity_card(self):
        """Test IT_IDENTITY_CARD functionality"""
        valid_cards = [
            "CA12345AB",
            "AB54321CD",
        ]
        for card in valid_cards:
            with self.subTest(card=card):
                text = f"Carta d'identità: {card}"
                results = analyze_text(text, ["IT_IDENTITY_CARD"])
                self.assertEqual(len(results), 1)
                self.assertEqual(results[0].entity_type, "IT_IDENTITY_CARD")
                self.assertEqual(text[results[0].start:results[0].end], card)
                self.assertGreater(results[0].score, 0)

        invalid_cards = [
            "XZ12",
            "12345ABCD",
            "ABCDE1234",
        ]
        for card in invalid_cards:
            with self.subTest(card=card):
                results = analyze_text(
                    f"Carta d'identità: {card}",
                    ["IT_IDENTITY_CARD"],
                )
                self.assertEqual(results, [])

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""
        test_str = "My Italian passport number is YA1234567"
        result = analyze_text(test_str, ["IT_PASSPORT"])
        self.assertEqual(result[0].entity_type, "IT_PASSPORT")

        #negative case
        test_str = "Hello, my name is John Smith."
        result = analyze_text(test_str, ["IT_PASSPORT"])
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
