#!/usr/bin/env python3
""" Parses maps and fixes step_ error. """

import urllib.request
import sys

to_parse = str(sys.argv[1])
print("Downloading %s" % to_parse)

# Download file, parse, then store.

request = urllib.request.urlopen(to_parse)

print("Parsing file.")

file_data = request.read().decode('utf-8')
file_data = file_data.replace("step_x", "pixel_x")
file_data = file_data.replace("step_y", "pixel_y")

print("Writing file.")
# Store file

with open("MiniStation.dmm", mode='w') as output_file:
    output_file.write(file_data)
