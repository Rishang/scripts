# crontab

#!/usr/bin/bash
# source ~/.bashrc
# export DISPLAY=:0
# eval "export $(egrep -z DBUS_SESSION_BUS_ADDRESS /proc/$(pgrep -u $LOGNAME gnome-session)/environ)";
# /usr/bin/notify-send -i  appointment  -c "im" "TAKE A BREAK it's Been 30 min, Get Up"


# tmux
export SHELL=/bin/bash

# sleep 1800 = 30min
# sleep 60 = 1min

count=0
limit=1800

while true;do
	sleep 60
	count=$(($count+60))
	if [[ $((count%300)) -eq 0 ]];then
		echo "$((count/60)) min complited"
	fi
	if [[ $count -eq $limit  ]];then
		# /usr/bin/notify-send "TAKE A BREAK it's Been 30 min, Get Up"
		x-www-browser --no-sandbox $HOME/.takeBreak/getUp.html ;
		clear
		echo "Done $((count/60)) min !!"
		sleep 300
		count=0
	fi

done
