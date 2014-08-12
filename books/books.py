#!/usr/bin/python

import os, sys, getopt

def read(rootdir):
    book_list = []
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            f = open(subdir+file, "r")
            if f.mode == "r":
                for line in f:
                    book_list.append(line)
            f.close()
    return book_list

def parse(book_list):
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
            raise TypeError("Unable to parse data. Please use known delimeter.")

    return clean_list

def command_help():
    print """Command to print out list of books.  Acceptable arguments:
        -h [or] --help:  Prints this text.
        --year:  Sorts by year in ascending order.
        --reverse:  Sorts by year in descending order.
        --filter [argument]:  Filters list by argument.
            ex.  python books --filter Agile
        """


def command_year(clean_list, reverse=False):
    new_list = sorted(clean_list, key=lambda k: k['Year'], reverse=reverse)
    print_list(new_list)

def command_filter(arg):
    print "filter"
    print arg

def print_list(final_list):
    for f in final_list:
        print (f["Last"] + ", "
               + f["First"] + ", "
               + f["Title"] + ", "
               + str(f["Year"]))

def main(argv):
    print "script running"
    root = "src/"
    book_list = [b.rstrip() for b in read(root)]
    clean_list = parse(book_list)

    opts, args = getopt.getopt(argv, 'h', ['help', 'filter=', 'year', 'reverse'])

    if opts:
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                command_help()
            if opt == "--filter":
                command_filter(arg)
            if opt == "--year":
                command_year(clean_list)
            if opt == "--reverse":
                command_year(clean_list, True)
    else:
        print_list(clean_list)


if __name__ == "__main__":
    main(sys.argv[1:])




