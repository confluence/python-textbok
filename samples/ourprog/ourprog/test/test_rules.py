import unittest
from ourprog.rules import Person

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person("Jane", "Smith")

    def test_init(self):
        self.assertEqual(self.person.name, "Jane")
        self.assertEqual(self.person.surname, "Smith")

    def test_fullname(self):
        self.assertEqual(self.person.fullname("Ms"), "Ms Jane Smith")
        self.assertEqual(self.person.fullname("Mrs"), "Mrs Jane Smith")
        self.assertRaises(ValueError, self.person.fullname, "HRH")
