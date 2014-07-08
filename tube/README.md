## tube.vim

*Tube* provides a tiny interface for sending commands from MacVim to a separate
iTerm or Terminal window without losing focus of MacVim.

### Installation

Install with [Vundle](https://github.com/gmarik/vundle), [Pathogen](https://github.com/tpope/vim-pathogen)
or [Neobundle](https://github.com/Shougo/neobundle.vim).

By default *Tube* sends commands to `Terminal.app` but if you prefer using
`iTerm.app` set the following variable in your `.vimrc` file:

    let g:tube_terminal = "iterm"

### Basic usage

To send commands to a separate terminal window use the `:Tube` command:

    :Tube echo "Hello world!"

This executes the given command in a separate terminal window without losing focus
of MacVim. If the window does not exist yet, then it is created.

Some characters have a special meaning and are expanded as described below:

* `%`: this character is replaced with current buffer name.

* `@`: this character is replaced with current selection (or the current
line if nothing is currently selected).

* `<cr>`: this character sequence is replaced with a carriage return.

**NOTE**: if you want to avoid expansion of certain characters escape them
with a backslash.

### Other useful commands

`:TubeClr [command]` executes the given command as `:Tube` would, but clears the
terminal screen before executing the command.

`:TubeLastCmd` executes the last executed command.

`:TubeCd` `cd`s into the container directory of the current buffer.

`:TubeInterrupt` interrupts the current running command by triggering `CTRL+C`
inside the terminal.

`:TubeFocus` gives focus to the terminal window.

`TubeClose` closes the terminal.

### Aliasing

With the option `g:tube_aliases` you can set shortcuts for executing frequently
executed commands.

    let g:tube_aliases = {
        \ "cmd1": "long command",
        \ "cmd2": "very long command",
    \ }

To execute an aliased command use the `:TubeAlias` command:

    :TubeAlias cmd1

To see what aliases are currently set, you can use the command `:TubeAliases`


