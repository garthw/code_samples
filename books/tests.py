#!/usr/bin/python

import books
import unittest
import sys

class TestBooks(unittest.TestCase):
    def setUp(self):
        self.file_root = "src/"
        self.book_list = books.read(self.file_root)
        print "in setup"


    def test_read(self):
        # Assert able to open and construct list in setup
        self.assertIsInstance(self.book_list, list)
        self.assertGreater(len(self.book_list), 0)


    def test_parse(self):
        # Assert having no delimeter raises TypeError
        bad_list = ["Test Data With No Delimeter"]
        self.assertRaises(TypeError, books.parse, bad_list)
        parsed_list = books.parse(self.book_list)
        # Assert parsed list returns list with values
        self.assertIsInstance(parsed_list, list)
        self.assertGreater(len(parsed_list), 0)
        # Assert list items are dictionaries with key/values
        self.assertIsInstance(parsed_list[0], dict)
        self.assertGreater(len(parsed_list[0]), 0)


    def test_command_help(self):
        return_string = books.command_help()
        self.assertIsInstance(return_string, str)
        self.assertGreater(len(return_string), 0)


    def test_command_year(self):
        pass


    def test_command_filter(self):
        pass


    def test_print_list(self):
        pass


    def test_main(self):
        pass

if __name__ == "__main__": unittest.main()