#!/usr/bin/python
# Files by Garth Whitten
# Using Python 2.7.5

import os
import sys
import getopt


def read(rootdir):
    # Loops through rootdir opening and appending text by line
    book_list = []
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            f = open(subdir + file, "r")
            if f.mode == "r":
                for line in f:
                    book_list.append(line)
            f.close()
    return book_list


def parse(book_list):
    # Parses through expected delimiters and order
    # Returning a cleaned list of books
    clean_list = []
    for book in book_list:
        if "," in book:
            book = book.split(",")
            clean_book = {"Last": book[1].strip(),
                          "First": book[2].strip(),
                          "Title": book[0].strip(),
                          "Year": int(book[3])}
            clean_list.append(clean_book)
        elif "|" in book:
            book = book.split("|")
            clean_book = {"Last": book[1].strip(),
                          "First": book[0].strip(),
                          "Title": book[2].strip(),
                          "Year": int(book[3])}
            clean_list.append(clean_book)
        elif "/" in book:
            book = book.split("/")
            clean_book = {"Last": book[2].strip(),
                          "First": book[1].strip(),
                          "Title": book[3].strip(),
                          "Year": int(book[0])}
            clean_list.append(clean_book)
        else:
            raise TypeError("Unable to parse data. Check delimeter.")

    return clean_list


def command_help():
    # Returns a formatted  string
    return """Command to print out list of books.  Acceptable arguments:
        -h [or] --help:  Prints this text.
        --year:  Sorts by year in ascending order.
        --reverse:  Sorts by year in descending order.
        --filter [argument]:  Filters list by argument.
            ex.  python books.py --filter Agile
        **** NOTE: --filter is chainable with --year OR --reverse  ***
        """


def command_year(clean_list, reverse=False):
    # Sorts items by year with optional reverse flag
    new_list = sorted(clean_list, key=lambda k: k['Year'], reverse=reverse)
    return new_list


def command_filter(clean_list, arg):
    # Searches through list returning items
    # that match query
    filtered_list = []
    for c in clean_list:
        for v in c.iteritems():
            if str(arg) in str(v[1]) and c not in filtered_list:
                filtered_list.append(c)
    return filtered_list


def print_list(final_list):
    # Returns formatted list
    for f in final_list:
        print (f["Last"] + ", "
               + f["First"] + ", "
               + f["Title"] + ", "
               + str(f["Year"]))


def last_name_sort(final_list, reverse=False):
    sorted_list = sorted(final_list, key=lambda k: k['Last'], reverse=reverse)
    return sorted_list


def main(argv):
    # Main Function Call
    # Returns list of books with optional sorting and filtering
    root = "src/"
    book_list = [b.rstrip() for b in read(root)]
    clean_list = parse(book_list)
    sorted_list = last_name_sort(clean_list)

    try:
        opts, args = getopt.getopt(argv, 'h', ['help', 'filter=',
                                               'year', 'reverse'])
        if opts:
            for opt, arg in opts:
                if opt in ("-h", "--help"):
                    print command_help()
                    return None
                if opt == "--filter":
                    sorted_list = command_filter(sorted_list, arg)
                if opt == "--year":
                    sorted_list = command_year(sorted_list)
                elif opt == "--reverse":
                    sorted_list = command_year(sorted_list, True)
                    sorted_list = last_name_sort(sorted_list, True)


        print_list(sorted_list)

    except Exception as e:
        print "Oops!  Encountered an error: {}".format(e)


if __name__ == "__main__":
    main(sys.argv[1:])
