#! /usr/bin/env python3

import os

HOME = os.environ.get("HOME")

app_category="Application"
print("Enter Application Name:",end='')
app_name=input()
print("Enter Application Path:",end='')
app_exec=input()
print("Enter Application Icon:",end='')
app_icon=input()

desktop_s=f"""
#!/usr/bin/env {app_exec}
[Desktop Entry]
Type=Application
Name={app_name}
Exec="{app_exec}" %U
Icon={app_icon}
Categories=Application;
"""

with open(f"{HOME}/.local/share/applications/{app_name.replace(' ','_').lower()}.desktop",'w') as s:
    s.write(desktop_s)