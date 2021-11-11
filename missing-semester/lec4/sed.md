# SED:
sed stands for `stream line editor` which uses regex for pattern mathcing. 

## SED syntax: 
`sed 's/.*disconnected from//'`
Here,
		|--> "." means a character. 
		|--> "*" means a set of characters. 
		|--> "s" means substitute. 
	  |--> [] refers to match one of many differnet characters. 

### Example: 
```
echo 'aba' | sed 's/[ab]//g'
ba
echo 'bba' | sed 's/[ab]//g'
ba
```
