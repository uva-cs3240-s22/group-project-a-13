from django.test import TestCase

# Create your tests here.
class FirstTestCase(TestCase):
    def test_one(self):
        self.assertIs(True, True)