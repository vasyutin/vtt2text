import sys
import argparse
import webvtt
#import os

# -----------------------------------------------------------------------------
if __name__ != '__main__':
    sys.exit(1)

ArgParser = argparse.ArgumentParser(description='VTT to text subtitles converter. Version 0.1. Written by Sergey Vasyutin.')
ArgParser.add_argument('input_file', type = str, help = 'Source directory', dest = 'input')
Arguments = ArgParser.parse_args()

if Arguments.input == None or Arguments.input == '':
	print('Error! No input file is specified.', file = sys.stderr)
	ArgParser.print_help()
	sys.exit(1)

Subtitles = None
try:
	Subtitles = webvtt.read(Arguments.input)
except:
	Subtitles = None

if Subtitles == None:
	print('Error! Error reading file "' + Arguments.input + '".', file = sys.stderr)
	sys.exit(1)

vtt = webvtt.read('subtitles.vtt')
transcript = ""

lines = []
for line in vtt:
    # Strip the newlines from the end of the text.
    # Split the string if it has a newline in the middle
    # Add the lines to an array
    lines.extend(line.text.strip().splitlines())

# Remove repeated lines
previous = None
for line in lines:
    if line == previous:
       continue
    transcript += " " + line
    previous = line

print(transcript)

sys.exit(0)