#!/usr/bin/env python3
# This program was developed using python version 3.4.3
# Copyright (c) 2015-2016 Joshua Gutow under the MIT License

import subprocess
import argparse
import sys
import os

# Global flag to determine if the program should be verbose or not
VERBOSE = False



jfile  = "main"
blddir = "build/"
srcdir = "src/"
libs   = ":/home/joshua/lib/*"

# Reads the config file in the current directory
def load_config():

    # Set global vars
    global jfile
    global blddir
    global srcdir
    global classpath

    jfile = "PaintedImage"

# Prints the message if verbose mode is on
def verbose(msg):
    if VERBOSE:
        print(msg) 

# Nukes the build directory
def clean():
    path_list = lsfiles(blddir)
    dir_list = lsdirs(blddir)

    for obj in path_list:
        verbose("Deleting " + obj)
        os.remove(obj)

    for obj in dir_list:
        verbose("Deleting " + obj)
        os.rmdir(obj)

# Compiles the file that matches the filename
def build(filename):

    if not os.path.isdir(blddir):
        os.mkdir(blddir)

    compiler = "javac"
    j_file  = [srcdir + filename + ".java"]
    j_flags  = ["-d", blddir, "-cp", srcdir + libs, "-g", "-Xprefer:newer"]
    j_params = [compiler] + j_flags + j_file
    try:
        tmp = subprocess.call(j_params)
        verbose(" ".join(j_params))
    except subprocess.CalledProcessError:
        sys.exit(1) # Could not build a file needed

# Runs the build
def execute():
    params = ["java", "-cp", blddir + libs, jfile]
    verbose(" ".join(params) + "\n----Output Below----")
    try:
        subprocess.call(params)
    except subprocess.CalledProcessError:
        sys.exit(1) # Error when running the program

# Gets all the files in a dir tree where the given dir is the root
def lsfiles(directory):
     if directory[-1] != "/":
          directory = directory + "/"
     tmp = os.listdir(directory)
     ret = []
     for path in tmp:
          if os.path.isdir(directory + path):
               ret = ret + lsfiles(directory + path)
          else:
               ret.append(directory + path)
     return ret

# Gets all the directories under a parent directory
# List begins with the most nested directories
def lsdirs(directory):
    if directory[-1] != "/":
        directory = directory + "/"
    tmp = os.listdir(directory)
    ret = []
    for path in tmp:
        if os.path.isdir(directory + path):
            ret.append(directory + path)
            ret = lsdirs(directory + path) + ret
    return ret

# Main method of the program
def main():

    # Sets up the flags that can be passed to the build system
    parser = argparse.ArgumentParser(
        description="By default, this program will compile the project and then attempt to run it if the build succeeded.")
    parser.add_argument("-c", "--clean", action="store_true", 
        help="Deletes all build files")
    parser.add_argument("-r", "--run", action="store_true", 
        help="Attempts to run the project without building it first")
    parser.add_argument("-v", "--verbose", action="store_true", 
        help="Prints what the program is doing")
    parser.add_argument("-b", "--build", action="store_true",
        help="Builds the project")
    parser.add_argument("-f", "--fresh", action="store_true", 
        help="Deletes build files then recompiles the project")
    args = parser.parse_args()


    # Default: compile then run
    # --clean: clean up                                 --clean,   -c
    # --build: only build                               --build,   -b
    # --run: only run                                   --run,     -r
    # --fresh-build: clean up then compile then run     --fresh,   -f

    if args.verbose == True:
        global VERBOSE
        VERBOSE = True

    load_config()

    if not os.path.isdir("/home/joshua/lib/"):
        global libs
        libs = ""


    if args.clean:
        clean()
    elif args.build:
        build(jfile)
    elif args.run:
        execute()
    elif args.fresh:
        clean()
        build(jfile)
    else:
        build(jfile)
        execute()

# Runs the program
main()
