# Vim Navigation.

## Navigate through pages ...
`ctrl + u` - Navigate page up.
`ctrl + d` - Navigate page down.

## Use Curly Braces to navigate through para's ...
`CTRL + {` - Navigate whole para up at a time.
`CTRL + }` - Navigate whole para down at a time.

## Viewport navigation ...
`H` - navigates to top of the viewport.
`M` - navigates to middle of the viewport.
`L` - navigates to bottom of the viewport.

## Horizontal Navigation.

`0/$` - Navigates to the end of the line.
`^` - Navigates to the start of the line.
`w` - Jump to the next word.
`b` - Jump to the previous word.
`e` - Jump to the end of the word.

## Let VIM TYPE

Let us yank `y` something... after that go into insert mode and press
`CTRL-R` this will enable your registers meaning now if you press any
key like say `a` then the contents of register `a` will get pasted in
the buffer.

* **STEP 1:** Yank something into a particular register.

`"byy` --> This will enable your `reg b` after that you need to type `yy` to
yank it into the `reg b`.

* **STEP 2:** Paste While You are in Insert Mode.

To paste the contents of `reg b` you need to type `CTRL + R` and then
the name of the specific register which is `b` in this case.

## The 'G' Key ...

`guu` - Converts everything into Lowercase.

`gUU` - Converts everything into Uppercase.

`g?` - Convert everything into rot13.


