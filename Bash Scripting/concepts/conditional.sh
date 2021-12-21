#!/bin/bash

# if else conditional statements. 

## if [ condition ];
## then
## 	statements
## fi

name='hmm'

if [ "$name" = hmm ];
then 
	echo "### Owner is back !!! ###"
	echo "Username: Hmm"
fi 

# IF-ELSE CONDITION

## if [ condition ]; 
## then 
##   statements
## else
##   statements
## fi

read -p "Enter Your Username: " user

if [ "$user" = "Elliot" ];
then 
  echo "### Mr.Robot is here ###" 
  echo "Username: $user"
else
  echo "Invalid User, Try again"
fi










