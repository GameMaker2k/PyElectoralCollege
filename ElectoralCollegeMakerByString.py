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

    $FileInfo: ElectoralCollegeMakerByString.py - Last Update: 11/16/2016 Ver. 0.0.1 RC 1 - Author: joshuatp $
'''

from __future__ import division, absolute_import, print_function;
import os, sys, re, argparse, ElectoralCollegeMakerLibrary;

parser = argparse.ArgumentParser(conflict_handler = "resolve", add_help = True);
parser.add_argument("-n", "--candidate-names", default = "Hillary Clinton,Donald Trump", help = "enter candidate names");
parser.add_argument("-s", "--candidate-short-names", default = "Clinton,Trump", help = "enter candidate short names");
parser.add_argument("-c", "--candidate-colors", default = "#698DC5,#F07763", help = "enter candidate colors");
parser.add_argument("-e", "--candidate-electoral-points", default = "0,0", help = "enter candidate electoral points");
parser.add_argument("-w", "--winning-candidate-states", default = "1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,1,1,1", help = "enter winning candidate states");
parser.add_argument("-p", "--electoral-college-points", default = "3,9,6,11,55,9,7,3,3,29,16,4,6,4,20,11,6,8,8,11,10,3,1,16,10,10,6,3,15,3,3,1,1,4,14,5,6,29,18,7,7,20,4,9,3,11,38,6,13,3,12,10,5,3", help = "enter electoral college points");
parser.add_argument("-i", "--state-initials", default = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY", help = "enter state initials");
parser.add_argument("-y", "--year", default = "2020", help = "enter presidential election year");
parser.add_argument("-o", "--output-file", action="store_true", help = "enter name of output image");
parser.add_argument("-op", "--output-png", action="store_true", help = "enter name of output image");
parser.add_argument("-v", "--version", action = "version", version = ElectoralCollegeMakerLibrary.__version__);
getargs = parser.parse_args();

if(getargs.output_png==False):
 print(ElectoralCollegeMakerLibrary.GenerateElectoralMap(getargs.candidate_names, getargs.candidate_short_names, getargs.candidate_colors, getargs.candidate_electoral_points, getargs.winning_candidate_states, getargs.electoral_college_points, getargs.state_initials, getargs.year, getargs.output_file));
if(getargs.output_png==True):
 print(ElectoralCollegeMakerLibrary.GenerateElectoralMapToPNG(getargs.candidate_names, getargs.candidate_short_names, getargs.candidate_colors, getargs.candidate_electoral_points, getargs.winning_candidate_states, getargs.electoral_college_points, getargs.state_initials, getargs.year));
