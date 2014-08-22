#!/usr/bin/python
# Using Python 2.7.5

import sys
import getopt


def main(argv):
    try:
        buffersize = 50000
        infile = open(argv[0], "rb")
        outfile = open(str(argv[0].split(".")[0]) + ".png", 'wb')
        buffer = infile.read(buffersize)
        while len(buffer):
            outfile.write(buffer)
            print "."
            buffer = infile.read(buffersize)
            print "Done"

    except Exception as e:
        print e

if __name__ == "__main__":
	main(sys.argv[1:])