
remove=`fd -HIg -t d "\.(venv|terraform|mypy_cache)$" $HOME  --regex -c never`

echo $remove | xargs rm -rf
