#!/usr/bin/env python
# Works in both python 2 and 3
import configparser
import sys
import os


# Create a config in ~/.WHATEVERCONFIG.conf with the following contents:
# [ssh]
# keyname = jimbo
# keypath = /Users/jimbo/.ssh/
# region = SOMEPLACEMAYBE
# zone = SOMECITYMAYBE


config = configparser.ConfigParser()
config.read(os.path.expanduser('~/.WHATEVERCONFIG.conf'))

sshkeylocation = config.get('ssh','keyname')
localsshkeypath = config.get('ssh', 'keypath') + sshkeylocation
region = config.get('ssh', 'region')
zone = config.get('ssh', 'zone')


# You now have those variables to play with