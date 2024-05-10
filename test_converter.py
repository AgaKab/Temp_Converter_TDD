import unittest
from converter import TemperatureConverter

class TestTemperatureConverter(unittest.TestCase):
    def setUp(self):
        self.converter = TemperatureConverter()
        
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(66, self.converter.celsius_to_fahrenheit(17))
    
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(32, self.converter.fahrenheit_to_celsius(96))
        
    def test_celsius_to_kelvin(self):
        self.assertEqual(290.15 ,self.converter.celsius_to_kelvin(17))
        
    def test_kelvin_to_celsius(self):
        self.assertEqual(17, self.converter.kelvin_to_celsius(290.15))
        
    def test_fahrenheit_to_kelvin(self):
        self.assertEqual(305.37, self.converter.fahrenheit_to_kelvin(90))
        
    def test_kelvin_to_fahrenheit(self):
       self.assertEqual(83.93, self.converter.kelvin_to_fahrenheit(302))

if __name__=="__main__":
    unittest.main()
            