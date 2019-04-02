#!/usr/bin/env python
"""Pomodoro App """


import argparse
import os
import datetime
import time
import gi
gi.require_version('Gio', '2.0')
from gi.repository import Notify

__author__ = "Tony Benoy"
__copyright__ = "Copyright 2019, Tony Benoy"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "me@tonybenoy.com"

def pomodoro(timer):
    Notify.init("Pomodoro Session Start")
    pom = Notify.Notification.new("Session started", "Session Started for"+str(timer/60))
    pom.show()
    f = open("log","a")
    f.write(str(datetime.datetime.now())+" : "+"Pomodoro started")
    try:
        time.sleep(timer)
        f.write(str(datetime.datetime.now())+" : " + "task done")
    except:
        f.write(str(datetime.datetime.now())+" : " + "Task Stopped")
        input("Continue?")
   f.close()

def breaktime(breakt) :
    Notify.init("Take a break")
    Hello = Notify.Notification.new("Take a Break!", "Take a break for."+str(breakt/60))
    Hello.show()
    f = open("log","a")
    f.write(str(datetime.datetime.now())+" : "+"Break started")
    try:
        time.sleep(breakt)
         f.write(str(datetime.datetime.now())+" : " + "Break Over")
    except:
        f.write(str(datetime.datetime.now())+" : " + "Break Stopped")
        input("Continue?")
    f.close()

parser =  argparse.ArgumentParser(description="Pomodoro Tool.")
parser.add_argument("-t", "--timer", type=int,default=25,help="Time for one pomodoro in minutes")
parser.add_argument("-b", "--breaktime",type=int,default=5, help="Time for short break in minutes.")
parser.add_argument("-c", "--consecutive",type=int,default=3, help="Number of tasks before long break.")
parser.add_argument("-n", "--task",type=int, default=4,help="Number of sessions.")
args = parser.parse_args()
args.breaktime*=60
args.timer*=60
file = open("log","a") 
file.write("Pomodoro  for : " + str(args.timer) + "Break for : "+str(args.breaktime)) 
file.close()
for i in range(1,args.task):
    pomodoro(args.timer)
    if i%args.consecutive==0:
        breaktime(args.breaktime*args.task)
    else:
        breaktime(args.breaktime)

