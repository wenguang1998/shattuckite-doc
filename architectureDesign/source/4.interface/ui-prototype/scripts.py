#!/usr/bin/python3
import os
import subprocess

htmlSet = [i for i in  os.listdir('./axure-generated') if ".html" in i]
for file in htmlSet:
    baseName = file.split('.')[0]
    with subprocess.Popen(["wkhtmltoimage","--crop-w","375",
    "./axure-generated/"+file,baseName+'.jpeg']) as proc:
        pass



