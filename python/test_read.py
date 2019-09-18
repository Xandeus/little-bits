#!/usr/bin/env python

import sys
import fileinput

for line in fileinput.input():
    print(line.count("0"))
