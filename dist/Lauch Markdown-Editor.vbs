Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "Markdown-Editor\Markdown-Editor.bat" & Chr(34), 0
Set WinScriptHost = Nothing
