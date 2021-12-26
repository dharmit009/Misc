#!/bin/bash

# SIMPLE PINGSWEEP ...
# read -p "Enter an IP Address: " ip; 
read -p "Enter your Subnet: " subnet; 

for ip in $(seq 250 254); 
do
	ping -c 1 $subnet.$ip 
done 

