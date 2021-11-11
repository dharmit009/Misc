#!/bin/bash 
counter=0; 
until [[ "$?" -ne 0 ]]; 
do
	counter=$((counter+1))
	./fail.sh &> out.txt
done

echo "The Script ran for $counter"
cat out.txt

