#!/bin/bash

# Va dans ton projet
cd ~/Documents/Code_Lab/Version_Control/Github/addlaseyne9

# Ouvre un nouveau terminal pour Tailwind
osascript <<EOF
tell application "Terminal"
    do script "cd ~/Documents/Code_Lab/Version_Control/Github/addlaseyne9 && pipenv run python manage.py tailwind start"
end tell
EOF

# Lance le serveur Django sur 0.0.0.0:8000
pipenv run python manage.py runserver 0.0.0.0:8000

