" ============================================================================
" File: plugin/tube.vim
" Description: MacVim and terminal interaction made easy
" Mantainer: Giacomo Comitti - https://github.com/gcmt
" Url: https://github.com/gcmt/tube.vim
" License: MIT
" ============================================================================


" Init
" ----------------------------------------------------------------------------

let s:current_folder = expand("<sfile>:p:h")

py import vim, sys
py sys.path.insert(0, vim.eval("s:current_folder"))

py import tube.core
py _tube = tube.core.Tube()


" Wrappers
" ----------------------------------------------------------------------------

function! tube#ExecuteCommand(start, end, args)
    py _tube.run_command(int(vim.eval('a:start')), int(vim.eval('a:end')), vim.eval('a:args'))
endfunction

function! tube#ExecuteCommandClear(start, end, args)
    py _tube.run_command(int(vim.eval('a:start')), int(vim.eval('a:end')), vim.eval('a:args'), clear=True)
endfunction

function! tube#ExecuteLastCommand()
    py _tube.run_last_command()
endfunction

function! tube#CdIntoCurrentDirectory()
    py _tube.cd_into(vim.eval('expand("%:p:h")'))
endfunction

function! tube#FocusTerminal()
    py _tube.focus_terminal()
endfunction

function! tube#InterruptRunningCommand()
    py _tube.interrupt_terminal()
endfunction

function! tube#CloseTerminal()
    py _tube.close_terminal()
endfunction

function! tube#ExecuteAlias(start, end, args)
    py _tube.run_alias(int(vim.eval('a:start')), int(vim.eval('a:end')), vim.eval('a:args'))
endfunction

function! tube#ExecuteAliasClear(start, end, args)
    py _tube.run_alias(int(vim.eval('a:start')), int(vim.eval('a:end')), vim.eval('a:args'), clear=True)
endfunction

function! tube#ShowAliases()
    py _tube.show_aliases()
endfunction
