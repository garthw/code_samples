#!/usr/bin/python
# Files by Garth Whitten
# Using Python 2.7.5

import books
import unittest
import random


class TestBooks(unittest.TestCase):
    def setUp(self):
        # Setup most commonly used values
        self.file_root = "src/"
        self.book_list = books.read(self.file_root)
        self.clean_list = books.parse(self.book_list)

    def test_read(self):
        # Assert able to open and construct list in setup
        self.assertIsInstance(self.book_list, list)
        self.assertGreater(len(self.book_list), 0)

    def test_parse(self):
        # Assert having no delimeter raises TypeError
        bad_list = ["Test Data With No Delimeter"]
        self.assertRaises(TypeError, books.parse, bad_list)
        parsed_list = books.parse(self.book_list)
        # Assert clean list returns list with values
        self.assertIsInstance(self.clean_list, list)
        self.assertGreater(len(self.clean_list), 0)
        # Assert list items are dictionaries with key/values
        self.assertIsInstance(self.clean_list[0], dict)
        self.assertGreater(len(self.clean_list[0]), 0)

    def test_command_help(self):
        return_string = books.command_help()
        # Assert help method returns string with value
        self.assertIsInstance(return_string, str)
        self.assertGreater(len(return_string), 0)

    def test_command_year(self):
        # Pick random integer between 0 and length of list
        start = random.randint(0, (len(self.clean_list) - 2))
        first = books.command_year(self.clean_list)[start]
        second = books.command_year(self.clean_list)[start + 1]
        # Assert year of random index is less than
        # or equal to year of following index
        self.assertLessEqual(first['Year'], second['Year'])
        # Assert year of random index is greater than or equal
        # to year of following index when reverse flag is True
        first = books.command_year(self.clean_list, True)[start]
        second = books.command_year(self.clean_list, True)[start + 1]
        self.assertGreaterEqual(first['Year'], second['Year'])

    def test_command_filter(self):
        good_filters = [99, "Martin", "Agile"]
        bad_filters = [200444, "Lorem Ipsum", "Nonsense-String"]
        # Test for results for values w/in list
        for good in good_filters:
            good_result = books.command_filter(self.clean_list, good)
            self.assertIsInstance(good_result, list)
            self.assertGreater(len(good_result), 0)
        # Test for no results for values outside of list
        for bad in bad_filters:
            no_result = books.command_filter(self.clean_list, bad)
            self.assertIsInstance(no_result, list)
            self.assertEqual(len(no_result), 0)

    def test_last_name_sort(self):
        # Pick random integer between 0 and length of list
        start = random.randint(0, (len(self.clean_list) - 2))
        first = books.last_name_sort(self.clean_list)[start]
        second = books.last_name_sort(self.clean_list)[start + 1]
        # Assert last name of random index is less than
        # or equal to last name of following index
        self.assertLessEqual(first['Last'], second['Last'])
         # Assert last name of random index is greater than or equal
        # to last name of following index when reverse flag is True
        first = books.last_name_sort(self.clean_list, True)[start]
        second = books.last_name_sort(self.clean_list, True)[start + 1]
        self.assertGreaterEqual(first['Last'], second['Last'])


if __name__ == "__main__":
    unittest.main()
