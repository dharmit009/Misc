bash is a programming language not a scripting language. 
root user id is 0. 

/sys has file for kernel parameters meaning you can change any parameter which is passed to kernel or set through kernel 

`echo 1060 | sudo tee brightness`

/sys/class/backlight/intel_backlight/brightness

bash treats '' and "" differently 
here is an example of the same .... 

# [Example 1]
Try echoing #!/bin/bash in double quotes using echo and see the output. 

`echo "#!/bin/bash"`

## Output: 
bash: Event not found !


# [Example 2]
Try echoing #!/bin/bash in single quotes using echo and see the output. 

`echo '#!/bin/bash'`

## Output 

/#!bin/bash
