#! /usr/bin/env python3

import os
import yaml


def main():

    """
    create gnome shortcurl 

    steps:
        - pip install pyyaml
        - create shortcut.yml
        - curl "https://raw.githubusercontent.com/Rishang/scripts/master/gnome_desktop_shortcut/create_shortcut.py" | python

    Example: shortcut.yml
        
        
        name: "standard-notes",
        exec: "/opt/appImages/standard-notes/standard-notes.AppImage",
        icon: "notes"

    """

    file_name = "shortcut.yml"
    if os.environ.get("SHORTCUT_YML"):
        file_name = os.environ.get("SHORTCUT_YML")

    with open(f"./{file_name}") as f:
        try:
            conf = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)

    HOME = os.environ.get("HOME")
    SHORTCUT_PATH = f"{HOME}/.local/share/applications"
    SHORTCUT_NAME:str = conf['name'].replace(' ','-').lower().capitalize()

    app_category = "Application"

    desktop_s = f"""
#!/usr/bin/env {conf["exec"]}

[Desktop Entry]
Type=Application
Name={conf["name"]}
Exec={conf["exec"]} %U
Icon={conf["icon"]}
Categories={app_category};

"""

    with open(f"{SHORTCUT_PATH}/{SHORTCUT_NAME}.desktop","w") as s:
        s.write(desktop_s)

    return

# exec
if os.path.isfile('shortcut.yml'):
    main()
else:
    raise Exception("required shortcut.yml at present directory, for one time run")
