import unittest
from calc import Calc

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_add(self):
        c = Calc(2,4)
        
        self.assertEqual(c.add(), 6)

    def test_i(self):
        c = Calc(8,9)
        self.assertEqual(c.get_i(), 8)
        self.assertTrue(isinstance(c, Calc))
        self.assertTrue(isinstance(self, TestStringMethods))
        self.assertTrue(isinstance(c.get_i(), int))


if __name__ == '__main__':
    unittest.main()
