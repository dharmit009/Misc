# VIM: 

## Terminologies: 

- What is a buffer ? 

A buffer contains the text of the file is what you actually edit. 

- What is a Window ? 

Displays a buffer. 

- What are Tabs ? 

A tab is more like a viewport. It's like having multiple windows. 

- What are splits ? 

Splits divide viewport into parts. 

% always points to your current file. 
^ always points to your past file. 

- What are alternative files ? 

- Jump List

## Gibberish Notes

gql --> converts long lines into paragraph (wrapping)

sort --> Select Lines with visual then press : and type sort anything 

.w !python --> will run the current line in python. 


### Marks: 
m[a-z] within buffer to mark buffers.
m[A-Z] within buffer to mark buffers.

'[a-zA-Z] jumps to the marked position. 


### Quickfix List: 

Do remember times when you have forgotten a file name and go through each file 
just to find the that one string of text or code that you wrote. We all have been 
there right? 

Thats were grep and ripgrep come in with quickfixlist they provide a quick list of 
items which contain your string. 

:grep "string" <path>
:copen 
:cnext or :cn 
:cprevious or :cp 
:cdo  \<checkout my your self\>

### Using Ripgrep with Quick fix list: 

>Rg <string you are lookig for> <directory path if any> 
**Example:**

>Rg pandas Python/\*.py


## Search and Replace: 

/s/foo/bar/
/s/foo/bar/g
/s/foo/bar/gc


if (foo){
  else if (bar){
  else if (baz){

      }
}

## Registers

:reg --> Lists all the registers. 
"byy --> Yank the contents into reg b

### editing macros using regs. 

"bp --> Paste the contents of reg b 
then you can edit it !!!


## Spell Checks within vim. 

One of the most under rated features of vim is it has inbuilt spell
checking system. To enable this feature all you need to do is add `set
spell` within your **.vimrc** file (which is generally located in your
home directory if not you can always create one). This will highlight
all the words which are misspelled. 

**Searching for misspelled words:**

`[s` is used to find misspelled words after the cursor (Forward
Search). 

`s]` is used to find misspelled words before the cursor (Backward
Search).

**Adding Custom words to Dictionary:**

To add custom words first of all we need to create a custom spell file
we do this by adding following to your **.vimrc**. 

``` vim

mkdir -p ~/.vim/spell
set spell spelllang=en_us
set spellfile=~/.vim/spell/en.utf-8.add

```
`zg` -> Used to add custom words to the dictionary 
`z=` -> Offers autocomplete suggestions with correct spellings. 
`zug` -> You can also remove words from the dictionary. 


## Twitchtubers: 
- thePrimegan 
- Teej 
- rwxrob




