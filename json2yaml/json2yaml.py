#!/usr/bin/python3

'''
chmod +x json2yaml.py
ln -s json2yaml.py ~/.local/bin

# use

cat example.json | json2yaml

cat example.json | json2yaml > example.yaml
'''

import yaml, json
import sys

if not sys.stdin.isatty():
    yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)
else:
    print("no stdin data")
