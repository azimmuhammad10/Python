#minimise all windows
powershell -command "& { $x = New-Object -ComObject Shell.Application; $x.minimizeall() }"