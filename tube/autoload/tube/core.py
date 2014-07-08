# -*- coding: utf-8 -*-
"""
tube.core
~~~~~~~~~

This module defines the Tube class.
"""

import vim
import shlex
import subprocess

from tube.utils import v
from tube.utils import expand
from tube.utils import options


class Tube:

    def __init__(self):
        self.last_command = ''
        self.term = options.get('terminal').lower()
        loc = vim.eval('globpath(&rtp, "autoload/tube")') + "/applescript/"
        self.BASE_CMD = "osascript {0}{1}.applescript".format(loc, self.term)
        self.BASE_CMD_INLINE = "osascript -e"

    def run_command(self, start, end, command, clear=False):
        """To execute the given command."""
        self.last_command = command

        if not command:
            self.open_terminal()
            return

        buf = vim.current.buffer
        bufname = buf.name if buf.name else ""
        selection = '\n'.join(buf[start-1:end])

        command = expand.cr(command)
        command = expand.character(command, '%', bufname)
        command = expand.character(command, '@', selection)

        if options.get('always_clear_screen', bool):
            clear = True

        self.run(command, clear=clear)

    def run_alias(self, start, end, alias, clear=False):
        """To execute the command associated to the given alias."""
        command = options.get('aliases').get(alias)
        if command:
            self.run_command(start, end, command, clear)
        else:
            v.echo("Alias '{0}' not found.".format(alias))

    def run_last_command(self):
        """To execute the last executed command."""
        if self.last_command:
            self.run_command(1, 1, self.last_command)
        else:
            v.echo("It seems that you haven't executed a command yet")

    def run(self, command, clear=False):
        """To execute the command in the terminal."""
        cmd = '{0} "{1}"'.format(self.BASE_CMD, command.replace('"', '\\"'))
        cmd = shlex.split(cmd)
        subprocess.call(["clear;"] + cmd if clear else cmd)

    def cd_into(self, path):
        """To `cd` into the give path."""
        self.run_command(1, 1, "cd {0}".format(path))

    def interrupt_terminal(self):
        """To interrupt the running command in the terminal window."""
        scpt = """
        tell application "{0}" to activate
        tell application "System Events"
            keystroke "c" using control down
        end tell
        tell application "MacVim" to activate"""
        cmd = "{0} '{1}'".format(self.BASE_CMD_INLINE, scpt.format(self.term))
        subprocess.call(shlex.split(cmd))

    def open_terminal(self):
        """To open the terminal."""
        scpt = """
        tell application "{0}" to activate
        tell application "MacVim" to activate"""
        cmd = "{0} '{1}'".format(self.BASE_CMD_INLINE, scpt.format(self.term))
        subprocess.call(shlex.split(cmd))

    def focus_terminal(self):
        """To give focus to the terminal."""
        scpt = 'tell application "{0}" to activate'.format(self.term)
        cmd = "{0} '{1}'".format(self.BASE_CMD_INLINE, scpt)
        subprocess.call(shlex.split(cmd))

    def close_terminal(self):
        """To close the terminal."""
        scpt = 'tell application "{0}" to quit'.format(self.term)
        cmd = "{0} '{1}'".format(self.BASE_CMD_INLINE, scpt)
        subprocess.call(shlex.split(cmd))

    def show_aliases(self):
        """To show all defined aliases."""
        aliases = options.get('aliases')
        if aliases:
            print('+ aliases')
            for i, alias in enumerate(aliases):
                conn = '└─ ' if i == len(aliases)-1 else '├─ '
                print(conn + alias + ': ' + aliases[alias])
        else:
            v.echo('No aliases found.')
