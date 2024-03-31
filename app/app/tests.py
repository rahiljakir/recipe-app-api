from django.test import SimpleTestCase

from . import calc

class CalcTest(SimpleTestCase):
    def test_add(self):
        res = calc.add(5,6)
        self.assertEqual(res,11)

    def test_subtract(self):
        res = calc.sub(10,15)
        self.assertEqual(res,5)