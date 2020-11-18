#!/usr/bin/env python

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2016 JoshuaTP - http://idb.berlios.de/
    Copyright 2016 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2016 Joshua Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: ElectoralCollegeMakerByYear.py - Last Update: 11/16/2016 Ver. 0.0.1 RC 1 - Author: joshuatp $
'''

from __future__ import division, absolute_import, print_function;
import os, sys, re, argparse, ElectoralCollegeMakerLibrary;

parser = argparse.ArgumentParser(conflict_handler = "resolve", add_help = True);
parser.add_argument("-y", "--year", default = "2020", help = "enter presidential election year");
parser.add_argument("-o", "--output-file", action="store_true", help = "enter name of output image");
parser.add_argument("-op", "--output-png", action="store_true", help = "enter name of output image");
parser.add_argument("-v", "--version", action = "version", version = ElectoralCollegeMakerLibrary.__version__);
getargs = parser.parse_args();

if(getargs.output_png==False):
 print(ElectoralCollegeMakerLibrary.GenerateElectoralMapByYear(getargs.year, getargs.output_file));
if(getargs.output_png==True):
 print(ElectoralCollegeMakerLibrary.GenerateElectoralMapByYearToPNG(getargs.year));
