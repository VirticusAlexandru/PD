# test_date_utils.py

import unittest
from datetime import datetime, timedelta
from date_utils import format_current_date, calculate_date_difference

class TestDateUtilsFunctions(unittest.TestCase):

    def test_format_current_date_default_format(self):
        formatted_date = format_current_date()
        self.assertIsInstance(formatted_date, str)

    def test_format_current_date_custom_format(self):
        custom_format = "%Y-%m-%d"
        formatted_date = format_current_date(custom_format)
        self.assertIsInstance(formatted_date, str)

    def test_calculate_date_difference(self):
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 1, 15)
        date_diff = calculate_date_difference(start_date, end_date)
        self.assertIsInstance(date_diff, timedelta)

        # Проверка, что разница между датами действительно равна 14 дням
        self.assertEqual(date_diff, timedelta(days=14))

if __name__ == '__main__':
    unittest.main()
