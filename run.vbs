Dim o
Set o = WScript.CreateObject ("WSCript.shell")
o.run "python totp.py",0,false
Set o = Nothing

'made by hageron