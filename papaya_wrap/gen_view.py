#!/usr/bin/env python3

import sys
import json
import os
import argparse
import pandas as pd
import shutil
import subprocess
import glob 

def path(string):
    if os.path.exists(string):
        return string
    else:
        sys.exit(f'File not found: {string}')

def console_tool():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bg', metavar='bg', type=path, \
        help='Path to input image (background).', required=True)
    parser.add_argument('--fg', metavar='fg', type=path, \
        help='Path to input image (overlay).', required=True)
    parser.add_argument('--out', metavar='out', type=str, \
        help='Path to output.', required=True)    
    parser.add_argument('--papaya', metavar='papaya', help='papaya scripts path', 
        type=str, default="/Users/ale/Desktop/projects/papaya_wrap/Papaya/")
    parser.add_argument('--template', metavar='template', \
        help='papaya html template path', type=str, default="{}/ref_build/index.html")
    parser.add_argument('--browser', metavar='browser', \
        help='browser to launch automatically created view', type=str, default=None)    
    parse_args, unknown = parser.parse_known_args()

    papaya, background, foreground = str(parse_args.papaya), str(parse_args.bg), str(parse_args.fg)
    parse_args.template = parse_args.template.format(papaya)

    # minimal error checks
    if not (parse_args.bg[-7:] == '.nii.gz' or parse_args.bg[-4:] == '.nii'):
        raise IOError('Input file (background) must be of type .nii or .nii.gz')

    if not (parse_args.fg[-7:] == '.nii.gz' or parse_args.fg[-4:] == '.nii'):
        raise IOError('Input file (overlay) must be of type .nii or .nii.gz')

    # 0 - prep images ?
    images = str(os.path.join(papaya, "images"))
    if os.path.isdir(images):
        shutil.rmtree(images)
    os.makedirs(images, exist_ok=True)

    background_ = str(os.path.join(images, "BG." + ".".join(str(background).split(".")[1:])))
    shutil.copyfile(background, background_)
    #... make it slimmer ?
    
    foreground_ = str(os.path.join(images, "FG." + ".".join(str(foreground).split(".")[1:])))
    shutil.copyfile(foreground, foreground_)
    #... make it slimmer ?

    # 1 - launch papaya building
    command = "cd {}; ./papaya-builder.sh -images {} {} -local".format(papaya, background_, foreground_)
    subprocess.call(command, shell=True)
    shutil.rmtree(images)

    # 2 - copy html template with toggle and local view to build folder
    shutil.copyfile(parse_args.template, str(os.path.join(papaya, "build", "index.html")))
    if not os.path.isdir(parse_args.out):
        os.makedirs(parse_args.out,exist_ok=True)
    for file_ in glob.glob(str(os.path.join(papaya, "build/*"))):
        shutil.copyfile(file_, str(os.path.join(parse_args.out,os.path.basename(file_))))
    
    # open up just created html
    if parse_args.browser:
        command = "{} {}".format(str(parse_args.browser), str(os.path.join(parse_args.out,"index.html")))
        subprocess.call(command, shell=True)
    
    
if __name__ == "__main__":
    try:
        console_tool()
    except Exception as e:
        print("Exception caught: " + str(e))
        sys.exit(1)
