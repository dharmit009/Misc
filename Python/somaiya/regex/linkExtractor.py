#!/bin/python3
import sys
from time import sleep

def helper():
    mess = """
Usage: python linkExtractor.py [OPTION]... [FILENAME]...
Link Extractor is used to extract links from files this is done using
regex and Python3. 

When no file is provided it asks for input remeber to keep
the file in same directory as the script. 

Options:
  -h, --help                  Shows this help menu.

"""
    print(mess)


def linkExtractor(data):
    links = list();
    for eachLine in data:
        links += re.findall("\w*\.['.com'| '.in' | '.net' | '.org' ]", eachLine)

    print(links)


if sys.argv == []: 
    fname = input("Enter File Name: ")
elif '-h' or '--help' in sys.argv: 
    helper()
else: 
    fname = sys.argv[1]


sleep(1)
data = open(fname);
linkExtractor(data);
data.close()

