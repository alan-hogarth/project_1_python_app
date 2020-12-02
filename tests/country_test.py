import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country = Country("Sweden")
    
    def test_country_has_name(self):
        self.assertEqual("Sweden", self.country.name)