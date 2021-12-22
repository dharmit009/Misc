#!/bin/python3

# Import regex ... 
import re
import sys
from time import sleep

# A Few test mails to visualize and create regex. 
"""
from: arjun email: arjun@test.com 
from: karan email: karan@test.com 
from: kamila email: kamila@test.com 

"""

def menu():
    mess = """
|#################################################|

                 ____           _ __
                / __/_ _  ___ _(_) /
               / _//  ' \/ _ `/ / / 
              /___/_/_/_/\_,_/_/_/  
                                    
       ____     __               __          
      / __/_ __/ /________ _____/ /____  ____
     / _/ \ \ / __/ __/ _ `/ __/ __/ _ \/ __/
    /___//_\_\\__/_/  \_,_/\__/\__/\___/_/   
                                             

|#################################################|                                                               
"""
    print(mess)
    sleep(1)

# TODO: To add sys.argv and fname to program with if else 
# conditions to execute properly. 
    fname = input("Enter a file name: "); 

# we will need to import the data first using open() ...
    data = open(fname);
    emailExtractor(data);

def helper():
    mess = """
Usage: python emailExtractor.py [OPTION]... [FILENAME]...
Email Extractor is used to extract emails from files this is done using
regex and Python3. 

When no file is provided it asks for input remeber to keep
the file in same directory as the script. 

Options:
  -h, --help                  Shows this help menu.

""";


def emailExtractor(data):
    emails = list();
    for eachLine in data:
        eachLine = eachLine.rstrip();
        emails += re.findall('\\S+@\\S+', eachLine);

    emails = sorted(set(emails));
    if emails != []:
        for xmails in emails:
            print(xmails);


menu();
