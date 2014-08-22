#!/usr/bin/python
# Using Python 2.7.5

import re
import collections

class CodeTest():

    def string_sub(self, search_string, char):
        if char in search_string:
            search_string = re.sub('['+ char + ']', '', search_string)        
            return search_string
        else:
            raise ValueError("'{}' not found in '{}'".format(char, search_string))


    def duplicate_list(self, search_list):
        return [x for x, y in collections.Counter(search_list).items() if y > 1]


    def map_roman(self, char):
        romanNumeralMap = {'M':  1000,
                           'CM': 900,
                           'D':  500,
                           'CD': 400,
                           'C':  100,
                           'XC': 90,
                           'L':  50,
                           'XL': 40,
                           'X':  10,
                           'IX': 9,
                           'V':  5,
                           'IV': 4,
                           'I':  1}
        roman_numeral_order = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')

        try:
            if type(char) == str:
                return_value = 0
                for index, character in enumerate(char):
                    previous = char[index - 1]
                    return_value += int(romanNumeralMap[character])
                    if ((character == "V" or character == "X") and (previous == "I")) \
                    or ((character == "L" or character == "C") and (previous == "X")) \
                    or ((character == "D" or character == "M") and (previous == "C")):
                        return_value -= (2 * int(romanNumeralMap[previous]))
                return return_value
            elif type(char) == int:
                return_value = ""
                if not 0 < char < 4000:
                    raise ValueError, "Argument must be between 1 and 3999"   
                ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
                nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
                return_value = ""
                for i in range(len(ints)):
                    count = int(char / ints[i])
                    return_value += nums[i] * count
                    char -= ints[i] * count
                return return_value
                    
        except Exception as e:
            print e



def main():
    code_test = CodeTest()
    print code_test.string_sub("this is a string", "s")

    print code_test.duplicate_list([1,2,4,5,1,2,3])

    print code_test.map_roman(1234)

    print code_test.map_roman("MMCCIV")






if __name__ == "__main__":
    main()