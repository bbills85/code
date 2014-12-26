#!/usr/bin/python

import subprocess

input = raw_input("Enter the directory you want listed: ")

subprocess.call("ls " + input, shell = True)
