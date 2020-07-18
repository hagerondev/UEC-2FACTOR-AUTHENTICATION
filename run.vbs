Dim o
Set o = WScript.CreateObject ("WSCript.shell")
o.run o.CurrentDirectory & "\do.bat",0
Set o = Nothing