import sys
import os
from time import sleep
import argparse
import subprocess

# use gnome-screensaver-command -l to lock the screen

def launch(website, sec):
    driver = subprocess.Popen(["firefox", website])
    sleep(sec)
    driver.terminate()


def cleanup():
    os.system("gnome-screensaver-command -l")


parser = argparse.ArgumentParser(description="Specify time unit; default is minutes.")
parser.add_argument("time", type=float, help="Length of time to run Netflix.")
parser.add_argument("--hours", help="Switch time unit to hours", action="store_true")
parser.add_argument("-w", "--website", help="Change website to run.")
args = parser.parse_args()


if args.website:
    site = args.website
else:
    site = "www.netflix.com"


if args.hours:
    time = int(args.time * 60 * 60)
    launch(site, time)
else:
    time = int(args.time * 60)
    launch(site, time)


cleanup()

