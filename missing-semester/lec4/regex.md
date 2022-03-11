# Regular Expression:

Regular expressions are also known as `Regex` which are used for pattern matching. 

## How does regex work ? 

Regex uses ASCII table character for pattern matching. This table include normal letters, numbers and symbols too. Regex is not about strings it is more about characters as essentially everything is a string. 

> *Note:* _Regex only supports infix mode it cannot work with postfix or prefix notation._


## Regex Basics: 

* `\d`         --> can be used to represent any character from 0 to 9.
* `\D`         --> can be used to represent any non numeric character.
* `.`          --> is used to represent wildcard.
* `\`          --> are used as an escape sequence.
* `^`         --> Used to check the start of the line.
* `$`         --> Used to check the end of the line.
* `[]`         --> square brackets are used to match specific set of data.
* `[^]`        --> The caret is used to exclude specific set of data.
* `\w`         --> can be used to represent any non alphanumeric character. 
* `\W`         --> can be used to represent any non alphanumeric character. 
* `a{n}`       --> Used to find repetitions.
* `{m,n}`      --> Used to find repetitions can also have a range from m,n. 
* `*`          --> Used to find zero or more repetitions. 
* `+`          --> Used to find one or more repetitions. 
* `?`          --> Used to represent optional character.  
* `()`         --> Used for capturing group and reference back. 
* `(a(bc))`    --> Used for capturing multiple groups and reference back. 
* `(.*)`       --> Used to capture all. 
* `(abc|def)`  --> Matches abc or def. 


## Whitespacing Regex: 

* `\t`      --> Used to represent 4 spaces or a shift tab.  
* `\n`      --> Used to represent new line. 
* `\r`      --> Used to represent carriage return. 
* `\s`      --> Used to represent whitespace or space. 
* `\S`      --> Used to represent non-whitespace or space. 


### Regex debugger:

- [Regex 101](https://regex101.com)
- [Regexone](https://regexone.com)
