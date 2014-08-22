#!/usr/bin/python

import unittest
import string_sub


class TestCodeTest(unittest.TestCase):
    def setUp(self):
        self.code_test = string_sub.CodeTest()

    def test_duplicate_list(self):
        self.assertEqual(self.code_test.duplicate_list([1,2,4,5,1,2,3]), [1,2])
        self.assertEqual(self.code_test.duplicate_list([555,1,2,555]), [555])
        self.assertEqual(self.code_test.duplicate_list([10,20,46,88,10,88]), [88,10])

    def test_convert_roman(self):
        self.assertEqual(self.code_test.map_roman(1234), "MCCXXXIV")
        self.assertEqual(self.code_test.map_roman("MMCCIV"), 2204)
        self.assertRaises(ValueError, self.code_test.map_roman(40000))



if __name__ == "__main__":
    unittest.main()