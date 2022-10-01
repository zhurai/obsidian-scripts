#!/usr/bin/python3
import os
file_path = os.path.dirname(os.path.abspath(__file__))
from includes import *
from string import Template

template_file="Journal-Personal.md"
script_dir = file_path
template_path = file_path+"/../02 Automation Templates"

with open(template_path+"/"+template_file,"r") as f:
    for line in f:
        print(line)

