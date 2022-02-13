# TMUX ...

## Basics ... 

Type `tmux` in order to start a tmux-session. You can also start a
tmux-session with a custom name if you wish to do so... You can do that
by typing: 

`tmux new -s session_name`

Here, `-s` stands for session. 

### Splits ...

**NOTE:** You need to start a session before performing any splits or else
it would not work. 

Splits are used to create panes within a window. You can create as many
panes as you need.

There are two types of split:

* Vertical Split:

To Perform a vertical split you need to press the following keychord: 
`CTRL + b + %`

* Horizontal Split. 

To Perform a vertical split you need to press the following keychord:
`CTRL + b + "`

### Pane Navigation ...

One of the most frustrating things about using a GUI is that we
typically use mouse in order to navigate not only it's time consuming
but it also breaks the workflow. The same goes for tmux though `tmux`
supports mouse it is still recommended to use keyboard shortcuts to
navigate the panes as it improves the overall productivity. 

There are a few different ways you can navigate between panes. Here are
some of them: 

* **Pane Navigation using tmux defaults:**

To toggle between different panes: 

`CTRL + b + < any arrow key >`

To toggle between different panes: 

`CTRL + b + o`

To toggle between different panes using numbers: 

`CTRL + b + q <number>`

* **Pane Navigation using vi mode:**

**NOTE:** There are a few things you need to note... Firstly you need to
add the following to the your configuration file. `.tmux.conf` (which
should be available in you home directory. If not then you need to
create one with empty content).

```
set -g mode-keys vi

```
Secondly, the vi mode offers a lot more features so it is presumed that
you already know what you are doing, and also have knowledge of vim and
it's keybindings.

To navigate using vim keybindings: 

`CTRL + b + < vim keybinding hjkl >`


