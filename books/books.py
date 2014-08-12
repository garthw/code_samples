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
            clean_book = {"Last": book[1],
                          "First": book[2],
                          "Title": book[0],
                          "Year": book[3]}
            clean_list.append(clean_book)
        elif "|" in book:
            book = book.split("|")
            clean_book = {"Last": book[1],
                          "First": book[0],
                          "Title": book[2],
                          "Year": book[3]}
            clean_list.append(clean_book)
        elif "/" in book:
            book = book.split("/")
            clean_book = {"Last": book[2],
                          "First": book[1],
                          "Title": book[3],
                          "Year": book[0]}
            clean_list.append(clean_book)
        else:
            raise TypeError("Unable to parse data. Please use known delimeter.")

    return clean_list

def command_help():
    print "help"

def command_year():
    print "year"

def command_filter(arg):
    print "filter"
    print arg

def command_reverse():
    print "reverse"

def main(argv):
    print "script running"
    root = "src/"
    book_list = [b.rstrip() for b in read(root)]
    clean_list = parse(book_list)

    print "_____ARGV____"
    print argv


    opts, args = getopt.getopt(argv, 'h', ['filter=', 'year', 'reverse'])

    for opt, arg in opts:
        if opt == "-h":
            command_help()
        if opt == "--filter":
            command_filter(arg)
        if opt == "--year":
            command_year()
        if opt == "--reverse":
            command_reverse()
    

if __name__ == "__main__":
    main(sys.argv[1:])





