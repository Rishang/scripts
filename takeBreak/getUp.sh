# crontab

#!/usr/bin/bash
# source ~/.bashrc
# export DISPLAY=:0
# eval "export $(egrep -z DBUS_SESSION_BUS_ADDRESS /proc/$(pgrep -u $LOGNAME gnome-session)/environ)";
# /usr/bin/notify-send -i  appointment  -c "im" "TAKE A BREAK it's Been 30 min, Get Up"


# tmux
source ~/.bashrc
let count=0
directory_name="$HOME/.takeBreak"
# sleep 1800 = 30min
# sleep 60 = 1min

while true;do
	sleep 60
	count=$(($count+60))
	if [[ $((count%300)) -eq 0 ]];then
		echo "$((count/60)) min complited"
	fi
	if [[ $count -eq 1800  ]];then
		# /usr/bin/notify-send "TAKE A BREAK it's Been 30 min, Get Up"
		xdg-open ${directory_name}/getUp.html ;
		clear
		echo "Done $((count/60)) min !!"
		sleep 300
		count=0
	fi

done
