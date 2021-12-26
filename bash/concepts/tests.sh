#!/bin/bash 

# `tests` are used to automating tasks that require 
# conditional statements

# take a look at `help test`
# -d checks for directory. 
# -e checks for file.

if [ -d ~/Test ]; 
then 
  echo "The Test directory Exists!"; 
else
  echo "Test folder not found."; 
fi 







