" ============================================================================
" File: plugin/tube.vim
" Description: MacVim and terminal interaction made easy
" Mantainer: Giacomo Comitti - https://github.com/gcmt
" Url: https://github.com/gcmt/tube.vim
" License: MIT
" ============================================================================


" Init
" ----------------------------------------------------------------------------

if exists("g:tube_loaded") || !has('python') || !has('gui_macvim') || &cp
    finish
endif
let g:tube_loaded = 1


" Options
" ----------------------------------------------------------------------------

let g:tube_terminal =
    \ get(g:, "tube_terminal", 'terminal')

let g:tube_always_clear_screen =
    \ get(g:, "tube_always_clear_screen", 0)

let g:tube_aliases =
    \ get(g:, "tube_aliases",  {})


" Commands
" ----------------------------------------------------------------------------

command! -nargs=* -range Tube call tube#ExecuteCommand(<line1>, <line2>, <q-args>)
command! -nargs=1 -range TubeAlias call tube#ExecuteAlias(<line1>, <line2>, <q-args>)
command! -nargs=* -range TubeClr call tube#ExecuteCommandClear(<line1>, <line2>, <q-args>)
command! -nargs=1 -range TubeAliasClr call tube#ExecuteAliasClear(<line1>, <line2>, <q-args>)
command! TubeLastCmd call tube#ExecuteLastCommand()
command! TubeInterrupt call tube#InterruptRunningCommand()
command! TubeCd call tube#CdIntoCurrentDirectory()
command! TubeFocus call tube#FocusTerminal()
command! TubeClose call tube#CloseTerminal()
command! TubeAliases call tube#ShowAliases()
