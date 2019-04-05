# Try it yourself, page 222

import unittest
from city_country import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for city_country.py"""

    def test_city_country(self):
        """Tests if the string 'Santiago, Chile' works"""
        city_name = city_country('santiago', 'chile')
        self.assertEqual(city_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Tests if the string 'Santiago, Chile - 5000000. works."""
        city_name = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(city_name, 'Santiago, Chile - 5000000.')