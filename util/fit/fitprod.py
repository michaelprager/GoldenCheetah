#!/bin/python3

import re
import time

print('{\n    "VERSION":' + str(int(time.time())) + ',')
print('    "PRODUCTS":[')

# output the known products captured by GoldenCheetah users
nongarmin = open("nongarmin.json", "r")
lines = nongarmin.readlines()
for line in lines:
    print("        " + line, end="")

# output garmin products as described in the FIT SDK
sdkheader = open("fit_example.h","r")
lines = sdkheader.readlines()
pre="        "
for line in lines:
    match = re.search("FIT_GARMIN_PROD", line)
    if match:
        name = re.search("(FIT_GARMIN_PRODUCT_)([^ \t]*)", line)
        id = re.search("\(FIT_GARMIN_PRODUCT\)([ 0-9]*)", line)
        if name and id:
            # extract name
            print(pre+ '{ "manu":1, "prod":' + id.group(1).strip() + ', "name":"' +  name.group(2).strip().replace('_',' ').title() + '" }', end="")
            pre=",\n        "
print("\n    ],\n")

# manufacturers list from FIT SDK

print('    "MANUFACTURERS":[')
pre="        "
for line in lines:
    match = re.search("FIT_MANUFACTURER_([^ \t]*).*\(\(FIT_MANUFACTURER\)([ 0-9]*)", line)
    if match:
        print(pre+ '{ "manu":' + match.group(2).strip() + ', "name":"' +  match.group(1).strip().replace('_',' ').title() + '" }', end="")
        pre=",\n        "

print("\n    ]\n}")

