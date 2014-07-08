-- terminal.applescript
---
-- this script requires an argument that represent the command to execute

on run argv

    set command to (item 1 of argv)

    tell application "Terminal"
        activate
        do script command in window 1
    end tell

    tell application "MacVim" to activate

end run
