import argparse
import os
import json
from pathlib import Path
import subprocess
import yt_dlp

# Parse args
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input file containing liked videos")
parser.add_argument("-s", "--store", help="Location of already stored liked videos")
parser.add_argument("-o", "--output", help="Location to download the new videos to")
args = parser.parse_args()

# Validate input
error = False
if args.input is None:
    print("Please provide and input file")
    error = True
elif not os.path.isfile(args.input):
    print("Input file provided does not exist")
    error = True
if args.output is None:
    print("Please provide an output directory")
    error = True
elif not os.path.isdir(args.output):
    print("Output directory provided does not exist")
    error = True
if error: exit

# Get list of files already stored on disk to filter from downloading
if (args.store is not None):
    storedFiles = [Path(f).stem for dp, dn, filenames in os.walk(args.store) for f in filenames]
    storedFiles = set(storedFiles)

# Parse JSON input file
input = open(args.input).read()
try:
    input = json.loads(input)
except:
    print("Error reading input file")
    raise

# Filter for videos not in the existing file store
logPath = os.path.join(args.output, "log.txt")
if args.store is not None:
    filtered = []
    for video in input:
        name = video["Name"]
        if name in storedFiles: 
            print("Skipping existing video: " + name)
            continue
        filtered.append(video)
    input = filtered
if len(input) = 0:
    print("No videos to process")
    sys.exit()
    
# Download videos
urls = []
for video in input:
    urls.append(video["URL"])
try:
    ydl_opts = {
        'outtmpl': os.path.join(args.output, "%(title)s.%(ext)s"),
        'ignore-errors': True,
        'continue': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)
except Exception as e:
    with open(logPath, "a") as logFile:
        logFile.write(str(e) + "\n")
