import unittest
from scholarship_checker import is_eligible_for_scholarship


class TestScholarshipEligibility(unittest.TestCase):
    def test_eligible_student(self):
        self.assertTrue(is_eligible_for_scholarship(3.8, 15000))

    def test_low_gpa(self):
        self.assertFalse(is_eligible_for_scholarship(3.4, 18000))

    def test_high_income(self):
        self.assertFalse(is_eligible_for_scholarship(3.6, 21000))

    def test_low_gpa_high_income(self):
        self.assertFalse(is_eligible_for_scholarship(3.2, 25000))

    def test_exact_threshold(self):
        self.assertTrue(is_eligible_for_scholarship(3.5, 20000))

    def test_invalid_gpa(self):
        with self.assertRaises(ValueError):
            is_eligible_for_scholarship(4.5, 15000)

    def test_negative_income(self):
        with self.assertRaises(ValueError):
            is_eligible_for_scholarship(3.8, -5000)

if __name__ == "__main__":
    unittest.main()
