#!/usr/bin/env python3
# Developed by Joshua Gutow. Copyright 2016 under the MIT License.

desc = '''This program helps you track the time you spend on something.
The file timer_log in the current directory is used to track the time spent.
The timer_log stoes the info in the following format: "[start/stop]:date\ttask"


Avaliable commands:
    start - log the current time as the start time.
    stop - log the current time as the end time.
    total - print out how much time has been spent.'''


import argparse
import time

# Sets up the arguments for the program.
def get_args():
    parser = argparse.ArgumentParser(description=desc,
                        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("CMD", nargs=1, help="Command to run")
    parser.add_argument("-t", "--task", nargs=1,
                        help="Specify the task that the time was spent on.")
    return parser.parse_args()

# Returns the file object for timer_log in append mode.
def open_time_log():
    try:
        f = open("timer_log", "a", encoding="utf-8")
        return f
    except:
        print("Couldn't open the timer log file")
        sys.exit(1)

# Writes the cmd, task, and current time to the file as described in the desc.
def write(cmd, task):
    f = open_time_log()

    msg = cmd + ":" + time.strftime("%Y-%m-%dT%H:%M:%S")
    if task != "":
        msg += "\t" + task
    msg += "\n"

    f.write(msg)
    f.close





write("start", "")
