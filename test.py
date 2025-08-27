import unittest
from main import suma, resta
class TestPrueba(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2,2),4)
    def test_resta(self):
        self.assertEqual(resta(4,2),2)

if __name__ == '__main__':  
    unittest.main()