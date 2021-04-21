# This script tell us every 30 min to take a small 5 min break

## Cuz sitting too much at computer is not good :)

### usage

command: `getup` on your terminal.
Creates a tmux session running a script every 30min.
which opens a 5min pop on browser, telling to take a small break

see if session in running
`tmux list-session | grep "getUP"`

To stop tmux session: `tmux kill-session -t getUP`

### install the scrip

1. `./setup.sh install`
2. restart your terminal
3. just type `getup` on your terminal to start session
 

### to remove setup configuration

`./setup.sh uninstall`
`tmux kill-session -t getUP`

### requirments
 
1. any Browser


2. tmux

### If you dont want to create variable and directly run it on shell, copy this

`echo "tmux new-session -d -s 'getUP' ~/takeBreak/getUp.sh'" >> ~/.bashrc`

