"""
Name            : testFinalShotsSystemBurgett.py
Author          : Chadwick Burgett
Created         : 04/24/2021
Course          : CIS 152 Data structures
Version         : 1.0
Copyright       : This is my own original work based on
                specifications issued by our instructor
                and ideas I researched on several different
                internet sites.
Description     : This is the UnitTest for the finalShotsSystemBurgett program. I only do tests
for the basic insert and remove because the program outputs random numbers and letters.
Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or
unmodified. I have not given other fellow student(s) access to
my program.
"""
import unittest
import unittest.mock as mock
from programs import finalShotsSystemBurgett as final


class TestCaseShots(unittest.TestCase):
    def test_add_shots(self):  # This tests adding shots.
        s = final.ShotsStack()
        s.push(5)
        with mock.patch('builtins.input', side_effect=[5]):
            self.assertEqual(s.size(), 5)

    def test_remove_shots(self):  # This tests removing shots.
        s = final.ShotsStack()
        s.push(5)
        s.pop(5)
        with mock.patch('builtins.input', side_effect=[5]):
            self.assertEqual(s.size(), 0)


class TestCasePeople(unittest.TestCase):
    def test_add_people(self):
        p = final.PriorityQueue()
        p.insert_persons(10)
        with mock.patch('builtins.input', side_effect=[5]):
            self.assertEqual(p.size(), 10)

    def test_remove_people(self):
        p = final.PriorityQueue()
        p.insert_persons(10)
        p.dequeue()
        with mock.patch('builtins.input', side_effect=[5]):
            self.assertEqual(p.size(), 9)


class TestCaseUserChoice(unittest.TestCase):
    def test_add_shots_with_empty(self):
        p = final.PriorityQueue()
        s = final.ShotsStack()
        with mock.patch('builtins.input', side_effect=[1, 10, p, s]):
            self.assertEqual(final.user_input(1, 10, p, s), "There are 10 shots left in the system.")

    def test_add_people_with_empty(self):
        p = final.PriorityQueue()
        s = final.ShotsStack()
        with mock.patch('builtins.input', side_effect=[2, 10, p, s]):
            self.assertEqual(final.user_input(2, 10, p, s), "There are 10 people left in the system.")


if __name__ == '__main__':
    unittest.main()
