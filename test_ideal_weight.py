import unittest
from ideal_weight_function import calculate_ideal_weight

class TestCalculateIdealWeight(unittest.TestCase):

    def test_male_normal_height(self):
        self.assertEqual(calculate_ideal_weight("male", 170), 67.8)

    def test_female_normal_height(self):
        self.assertEqual(calculate_ideal_weight("female", 170), 61.7)

    def test_boundary_height(self):
        self.assertEqual(calculate_ideal_weight("male", 152), 48)
        self.assertEqual(calculate_ideal_weight("female", 152), 45.5)

    def test_invalid_gender(self):
        with self.assertRaises(ValueError):
            calculate_ideal_weight("other", 170)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_ideal_weight("male", -10)

    def test_non_numeric_height(self):
        with self.assertRaises(ValueError):
            calculate_ideal_weight("female", "invalid")

if __name__ == "__main__":
    unittest.main()
