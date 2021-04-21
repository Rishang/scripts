#!/usr/bin/bash

# for ubuntu/debian
directory="$HOME/.takeBreak"
function _install 
{
	echo -e "Making directory ${directory}"
	if [[ -e ${directory}  ]];then
		echo -e "folder already exist, you might have to re-install setup, copy below line to do so."
		echo -e "\nbash setup.sh uninstall && bash setup.sh install"
		exit
	else
		mkdir -p ${directory}
	fi

	echo -e "\nsetting executable permition to getUp.sh"
	chmod +x getUp.sh

	echo -e "Copying all files present here to ${directory}\n"
	cp getUp.html getUp.sh README.md ${directory}

	if ! [ $(command -v tmux) ];then
	echo -e "installing tmux"
	sudo apt update;sudo apt install -y tmux
	fi
	echo -e "Setting up bash alias for starting Script in tmux session"

	if ! [[ $(grep '# takeBreak alias' ~/.bash_aliases) ]];then 
		echo 'Creating: # takeBreak alias >> ~/.bash_aliases'
		echo -e "# takeBreak alias" >> ~/.bash_aliases
		echo "alias getup='echo Take Break every 30min; tmux new-session -d -s "getUP" ${directory}/getUp.sh'" >> ~/.bash_aliases
	else
		echo 'alias "getup" already exist'
	fi

	echo -e "Done"
}

function _clean
{
	echo "Removing configs for getUp in bash_aliases, ${directory}"
	if [[ -e ${directory}  ]];then
		rm -rf ${directory}
	else
		echo -e "folder not found"
	fi

	if [ -e ~/.bash_aliases ];then
		sed -i '/# takeBreak alias/d' ~/.bash_aliases
		sed -i '/alias getup.*/d' ~/.bash_aliases
	else
		echo "~/.bash_aliases file not found"
	fi
}

case "$1" in
	install)
		_install
		exec bash -l
	;;

	uninstall)
		_clean
		exec bash -l

	;;

	*)
		echo "install:   bash setup.sh install"
		echo "uninstall: bash setup.sh uninstall"
	;;
esac
