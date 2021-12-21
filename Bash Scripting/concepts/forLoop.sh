#!/bin/bash

# for VAR in $();
# do
# 	statements; 
# done 

# for x in $( echo {1..10} );
# do 
# 	echo "x: $x" 
# done

for x in $(cat output.txt);
do
	echo -e "$x\n"
done

