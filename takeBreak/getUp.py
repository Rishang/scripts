#!/usr/bin/env python3
import os
import time
import webbrowser
import logging

min = 30
sleep = 60 * min

while True:
    time.sleep(sleep)
    print()
    logging.info(f'{min} min completed')
    webbrowser.open(url=f'{os.environ.get("HOME")}/.takeBreak/getUp.html')
