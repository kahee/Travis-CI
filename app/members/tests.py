from django.test import TestCase

# Create your tests here.
class Errorexec(TestCase):

    def check_number(self):
        num = 2

        self.assertEqual(num, 3)



