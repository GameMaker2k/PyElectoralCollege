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

    $FileInfo: ElectoralCollegeMakerLibrary.py - Last Update: 11/16/2016 Ver. 0.0.1 RC 1 - Author: joshuatp $
'''

from __future__ import division, absolute_import, print_function;
import os, sys, re, cairosvg;
from io import BytesIO, StringIO;

__version_info__ = (0, 0, 1, "RC 1");
if(__version_info__[3]!=None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2])+" "+str(__version_info__[3]);
if(__version_info__[3]==None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2]);
__project__ = "PyElectoralCollegeMaker";
__project_url__ = "https://github.com/GameMaker2k/PyXML-Draw";

def GenerateElectoralMapByYear(electoral_year, output_to_file=True):
 if(electoral_year=="1964"):
  candidate_names = "Lyndon B. Johnson,Barry Goldwater";
  candidate_short_names = "Johnson,Goldwater";
  candidate_colors = "#698DC5,#F07763";
  candidate_electoral_points = "0,0";
  winning_candidate_states = "0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0";
  electoral_college_points = "3,10,6,5,40,6,8,3,3,14,12,4,9,4,26,13,7,9,10,14,10,3,1,21,10,12,7,4,13,4,3,1,1,4,16,4,3,43,26,8,6,29,4,8,4,11,25,4,12,3,9,12,6,3";
  state_initials = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY";
  return GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file);
 if(electoral_year=="1968"):
  candidate_names = "Hubert Humphrey,Richard Nixon,George Wallace";
  candidate_short_names = "Humphrey,Nixon,Wallace";
  candidate_colors = "#698DC5,#F07763,#AF60AF";
  candidate_electoral_points = "0,0,0";
  winning_candidate_states = "1,2,2,1,1,1,0,0,1,1,2,0,1,1,1,1,1,1,2,0,0,0,0,0,0,1,2,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,1,0,1";
  electoral_college_points = "3,10,6,5,40,6,8,3,3,14,12,4,9,4,26,13,7,9,10,14,10,3,1,21,10,12,7,4,13,4,3,1,1,4,16,4,3,43,26,8,6,29,4,8,4,11,25,4,12,3,9,12,6,3";
  state_initials = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY";
  return GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file);
 if(electoral_year=="1972"):
  candidate_names = "George McGovern,Richard Nixon";
  candidate_short_names = "McGover,Nixon";
  candidate_colors = "#698DC5,#F07763";
  candidate_electoral_points = "0,0";
  winning_candidate_states = "1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1";
  electoral_college_points = "3,9,6,6,45,7,8,3,3,17,12,4,8,4,26,13,7,9,10,14,10,3,1,21,10,12,7,4,13,3,3,1,1,4,16,4,3,41,23,8,6,27,4,8,4,10,26,4,12,3,9,11,6,3";
  state_initials = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY";
  return GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file);
 if(electoral_year=="1976"):
  candidate_names = "Jimmy Carter,Gerald Ford";
  candidate_short_names = "Carter,Ford";
  candidate_colors = "#698DC5,#F07763";
  candidate_electoral_points = "0,0";
  winning_candidate_states = "1,0,0,1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,1,0,0,1,1,1,1,0,0,1";
  electoral_college_points = "3,9,6,6,45,7,8,3,3,17,12,4,8,4,26,13,7,9,10,14,10,3,1,21,10,12,7,4,13,3,3,1,1,4,16,4,3,41,23,8,6,27,4,8,4,10,26,4,12,3,9,11,6,3";
  state_initials = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY";
  return GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file);
 if(electoral_year=="1980"):
  candidate_names = "Jimmy Carter,Ronald Reagan,John B. Anderson";
  candidate_short_names = "Carter,Reagan,Anderson";
  candidate_colors = "#698DC5,#F07763,#C0C0C0";
  candidate_electoral_points = "0,0,0";
  winning_candidate_states = "1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1";
  electoral_college_points = "3,9,6,6,45,7,8,3,3,17,12,4,8,4,26,13,7,9,10,14,10,3,1,21,10,12,7,4,13,3,3,1,1,4,16,4,3,41,23,8,6,27,4,8,4,10,26,4,12,3,9,11,6,3";
  state_initials = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY";
  return GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file);
 if(electoral_year=="1984"):
  candidate_names = "Walter Mondale,Ronald Reagan";
  candidate_short_names = "Mondale,Reagan";
  candidate_colors = "#698DC5,#F07763";
  candidate_electoral_points = "0,0";
  winning_candidate_states = "1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1";
  electoral_college_points = "3,9,6,7,47,8,8,3,3,21,12,4,8,4,24,12,7,9,10,12,10,3,1,20,10,11,7,4,13,3,3,1,1,4,16,5,4,36,23,8,7,25,4,8,3,11,29,5,12,3,10,11,6,3";
  state_initials = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY";
  return GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file);
 if(electoral_year=="1988"):
  candidate_names = "Michael Dukakis,George H. W. Bush";
  candidate_short_names = "Dukakis,Bush";
  candidate_colors = "#698DC5,#F07763";
  candidate_electoral_points = "0,0";
  winning_candidate_states = "1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,0,0,0,1";
  electoral_college_points = "3,9,6,7,47,8,8,3,3,21,12,4,8,4,24,12,7,9,10,12,10,3,1,20,10,11,7,4,13,3,3,1,1,4,16,5,4,36,23,8,7,25,4,8,3,11,29,5,12,3,10,11,6,3";
  state_initials = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY";
  return GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file);
 if(electoral_year=="1992"):
  candidate_names = "Bill Clinton,George H. W. Bush,Ross Perot";
  candidate_short_names = "Clinton,Bush,Perot";
  candidate_colors = "#698DC5,#F07763,#C0C0C0";
  candidate_electoral_points = "0,0,0";
  winning_candidate_states = "1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,1,1,0,0,0,0,1";
  electoral_college_points = "3,9,6,8,54,8,8,2,3,25,13,4,7,4,22,12,6,8,9,12,10,3,1,18,10,11,7,3,14,3,3,1,1,4,15,5,4,33,21,8,7,23,4,8,3,11,32,5,13,3,11,11,5,3";
  state_initials = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY";
  return GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file);
 if(electoral_year=="1996"):
  candidate_names = "Bill Clinton,Bob Dole,Ross Perot";
  candidate_short_names = "Clinton,Dole,Perot";
  candidate_colors = "#698DC5,#F07763,#C0C0C0";
  candidate_electoral_points = "0,0,0";
  winning_candidate_states = "1,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,1,1,0,0,0,0,1";
  electoral_college_points = "3,9,6,8,54,8,8,2,3,25,13,4,7,4,22,12,6,8,9,12,10,3,1,18,10,11,7,3,14,3,3,1,1,4,15,5,4,33,21,8,7,23,4,8,3,11,32,5,13,3,11,11,5,3";
  state_initials = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY";
  return GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file);
 if(electoral_year=="2000"):
  candidate_names = "Al Gore,George W. Bush";
  candidate_short_names = "Gore,Bush";
  candidate_colors = "#698DC5,#F07763";
  candidate_electoral_points = "0,0";
  winning_candidate_states = "1,1,1,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1";
  electoral_college_points = "3,9,6,8,54,8,8,2,3,25,13,4,7,4,22,12,6,8,9,12,10,3,1,18,10,11,7,3,14,3,3,1,1,4,15,5,4,33,21,8,7,23,4,8,3,11,32,5,13,3,11,11,5,3";
  state_initials = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY";
  return GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file);
 if(electoral_year=="2004"):
  candidate_names = "John Kerry,George W. Bush";
  candidate_short_names = "Kerry,Bush";
  candidate_colors = "#698DC5,#F07763";
  candidate_electoral_points = "0,0";
  winning_candidate_states = "1,1,1,1,0,1,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1";
  electoral_college_points = "3,9,6,10,55,9,7,3,3,27,13,4,7,4,21,11,6,8,9,12,10,3,1,17,10,11,6,3,15,3,3,1,1,4,15,5,5,31,20,7,7,21,4,8,3,11,34,5,13,3,11,10,5,3";
  state_initials = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY";
  return GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file);
 if(electoral_year=="2008"):
  candidate_names = "Barack Obama,John McCain";
  candidate_short_names = "Obama,McCain";
  candidate_colors = "#698DC5,#F07763";
  candidate_electoral_points = "0,0";
  winning_candidate_states = "1,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1";
  electoral_college_points = "3,9,6,10,55,9,7,3,3,27,15,4,7,4,21,11,6,8,9,12,10,3,1,17,10,11,6,3,15,3,3,1,1,4,15,5,5,31,20,7,7,21,4,8,3,11,34,5,13,3,11,10,5,3";
  state_initials = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY";
  return GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file);
 if(electoral_year=="2012"):
  candidate_names = "Barack Obama,Mitt Romney";
  candidate_short_names = "Obama,Romney";
  candidate_colors = "#698DC5,#F07763";
  candidate_electoral_points = "0,0";
  winning_candidate_states = "1,1,1,1,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1";
  electoral_college_points = "3,9,6,11,55,9,7,3,3,29,16,4,6,4,20,11,6,8,8,11,10,3,1,16,10,10,6,3,15,3,3,1,1,4,14,5,6,29,18,7,7,20,4,9,3,11,38,6,13,3,12,10,5,3";
  state_initials = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY";
  return GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file);
 if(electoral_year=="2016"):
  candidate_names = "Hillary Clinton,Donald Trump";
  candidate_short_names = "Clinton,Trump";
  candidate_colors = "#698DC5,#F07763";
  candidate_electoral_points = "0,0";
  winning_candidate_states = "1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,1,1,1";
  electoral_college_points = "3,9,6,11,55,9,7,3,3,29,16,4,6,4,20,11,6,8,8,11,10,3,1,16,10,10,6,3,15,3,3,1,1,4,14,5,6,29,18,7,7,20,4,9,3,11,38,6,13,3,12,10,5,3";
  state_initials = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY";
  return GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file);
 if(electoral_year=="2020"):
  candidate_names = "Joe Biden,Donald Trump";
  candidate_short_names = "Biden,Trump";
  candidate_colors = "#698DC5,#F07763";
  candidate_electoral_points = "0,0";
  winning_candidate_states = "1,1,1,0,0,0,0,0,0,1,0,0,1,1,0,1,1,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1";
  electoral_college_points = "3,9,6,11,55,9,7,3,3,29,16,4,6,4,20,11,6,8,8,11,10,3,1,16,10,10,6,3,15,3,3,1,1,4,14,5,6,29,18,7,7,20,4,9,3,11,38,6,13,3,12,10,5,3";
  state_initials = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,ME-2,MI,MN,MO,MS,MT,NC,ND,NE,NE-1,NE-2,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY";
  return GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file);
 return False;

def GenerateElectoralMapByYearToPNG(electoral_year):
 outputsvg = GenerateElectoralMapByYear(electoral_year, False);
 if(outputsvg==False):
  return False;
 cairosvg.svg2png(bytestring=outputsvg.encode('utf-8'), write_to="ElectoralCollege"+electoral_year+".png");
 return True;

def GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, output_to_file=True):
 candidate_names_split = [x.strip() for x in candidate_names.split(',')];
 candidate_short_names_split = [x.strip() for x in candidate_short_names.split(',')];
 candidate_colors_split = [x.strip() for x in candidate_colors.split(',')];
 candidate_electoral_points_split = [x.strip() for x in candidate_electoral_points.split(',')];
 candidate_electoral_points_split = [int(x) for x in candidate_electoral_points_split];
 winning_candidate_states_split = [x.strip() for x in winning_candidate_states.split(',')];
 winning_candidate_states_split = [int(x) for x in winning_candidate_states_split];
 electoral_college_points_split = [x.strip() for x in electoral_college_points.split(',')];
 electoral_college_points_split = [int(x) for x in electoral_college_points_split];
 state_initials_split = [x.strip() for x in state_initials.split(',')];
 statemapoutput = "  <g id=\"outlines\">\n";
 statetextoutput = "  <g id=\"text\" font-family=\"Helvetica Neue\" font-size=\"28\" font-weight=\"bold\">\n";
 statemapoutput_dclast = "";
 statetextoutput_dclast = "";

 il = 0;
 ilx = len(winning_candidate_states_split);
 while(il < ilx):
  if(state_initials_split[il]=="AK"):
   statemapoutput = statemapoutput + "   <path id=\"AK\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M161.1,453.7l-0.3,85.4l1.6,1l3.1,0.2l1.5-1.1h2.6l0.2,2.9l7,6.8l0.5,2.6l3.4-1.9l0.6-0.2l0.3-3.1 l1.5-1.6l1.1-0.2l1.9-1.5l3.1,2.1l0.6,2.9l1.9,1.1l1.1,2.4l3.9,1.8l3.4,6l2.7,3.9l2.3,2.7l1.5,3.7l5,1.8l5.2,2.1l1,4.4l0.5,3.1 l-1,3.4l-1.8,2.3l-1.6-0.8l-1.5-3.1l-2.7-1.5l-1.8-1.1l-0.8,0.8l1.5,2.7l0.2,3.7l-1.1,0.5l-1.9-1.9l-2.1-1.3l0.5,1.6l1.3,1.8 l-0.8,0.8c0,0-0.8-0.3-1.3-1c-0.5-0.6-2.1-3.4-2.1-3.4l-1-2.3c0,0-0.3,1.3-1,1c-0.6-0.3-1.3-1.5-1.3-1.5l1.8-1.9l-1.5-1.5v-5h-0.8 l-0.8,3.4l-1.1,0.5l-1-3.7l-0.6-3.7l-0.8-0.5l0.3,5.7v1.1l-1.5-1.3l-3.6-6l-2.1-0.5l-0.6-3.7l-1.6-2.9l-1.6-1.1v-2.3l2.1-1.3 l-0.5-0.3l-2.6,0.6l-3.4-2.4l-2.6-2.9l-4.8-2.6l-4-2.6l1.3-3.2v-1.6l-1.8,1.6l-2.9,1.1l-3.7-1.1l-5.7-2.4h-5.5l-0.6,0.5l-6.5-3.9 l-2.1-0.3l-2.7-5.8l-3.6,0.3l-3.6,1.5l0.5,4.5l1.1-2.9l1,0.3l-1.5,4.4l3.2-2.7l0.6,1.6l-3.9,4.4l-1.3-0.3l-0.5-1.9l-1.3-0.8 l-1.3,1.1l-2.7-1.8l-3.1,2.1l-1.8,2.1l-3.4,2.1l-4.7-0.2l-0.5-2.1l3.7-0.6v-1.3l-2.3-0.6l1-2.4l2.3-3.9v-1.8l0.2-0.8l4.4-2.3l1,1.3 h2.7l-1.3-2.6l-3.7-0.3l-5,2.7l-2.4,3.4l-1.8,2.6l-1.1,2.3l-4.2,1.5l-3.1,2.6l-0.3,1.6l2.3,1l0.8,2.1l-2.7,3.2l-6.5,4.2l-7.8,4.2 l-2.1,1.1l-5.3,1.1l-5.3,2.3l1.8,1.3l-1.5,1.5l-0.5,1.1l-2.7-1l-3.2,0.2l-0.8,2.3h-1l0.3-2.4l-3.6,1.3l-2.9,1l-3.4-1.3l-2.9,1.9 h-3.2l-2.1,1.3l-1.6,0.8l-2.1-0.3l-2.6-1.1l-2.3,0.6l-1,1l-1.6-1.1v-1.9l3.1-1.3l6.3,0.6l4.4-1.6l2.1-2.1l2.9-0.6l1.8-0.8l2.7,0.2 l1.6,1.3l1-0.3l2.3-2.7l3.1-1l3.4-0.6l1.3-0.3l0.6,0.5h0.8l1.3-3.7l4-1.5l1.9-3.7l2.3-4.5l1.6-1.5l0.3-2.6l-1.6,1.3l-3.4,0.6 l-0.6-2.4l-1.3-0.3l-1,1l-0.2,2.9l-1.5-0.2l-1.5-5.8l-1.3,1.3l-1.1-0.5l-0.3-1.9l-4,0.2l-2.1,1.1l-2.6-0.3l1.5-1.5l0.5-2.6 l-0.6-1.9l1.5-1l1.3-0.2l-0.6-1.8v-4.4l-1-1l-0.8,1.5h-6.1l-1.5-1.3l-0.6-3.9l-2.1-3.6v-1l2.1-0.8l0.2-2.1l1.1-1.1l-0.8-0.5 l-1.3,0.5l-1.1-2.7l1-5l4.5-3.2l2.6-1.6l1.9-3.7l2.7-1.3l2.6,1.1l0.3,2.4l2.4-0.3l3.2-2.4l1.6,0.6l1,0.6h1.6l2.3-1.3l0.8-4.4 c0,0,0.3-2.9,1-3.4c0.6-0.5,1-1,1-1l-1.1-1.9l-2.6,0.8l-3.2,0.8l-1.9-0.5l-3.6-1.8l-5-0.2l-3.6-3.7l0.5-3.9l0.6-2.4l-2.1-1.8 l-1.9-3.7l0.5-0.8l6.8-0.5h2.1l1,1h0.6l-0.2-1.6l3.9-0.6l2.6,0.3l1.5,1.1l-1.5,2.1l-0.5,1.5l2.7,1.6l5,1.8l1.8-1l-2.3-4.4l-1-3.2 l1-0.8l-3.4-1.9l-0.5-1.1l0.5-1.6l-0.8-3.9l-2.9-4.7l-2.4-4.2l2.9-1.9h3.2l1.8,0.6l4.2-0.2l3.7-3.6l1.1-3.1l3.7-2.4l1.6,1l2.7-0.6 l3.7-2.1l1.1-0.2l1,0.8l4.5-0.2l2.7-3.1h1.1l3.6,2.4l1.9,2.1l-0.5,1.1l0.6,1.1l1.6-1.6l3.9,0.3l0.3,3.7l1.9,1.5l7.1,0.6l6.3,4.2 l1.5-1l5.2,2.6l2.1-0.6l1.9-0.8l4.8,1.9L161.1,453.7z M46,482.6l2.1,5.3l-0.2,1l-2.9-0.3l-1.8-4l-1.8-1.5H39l-0.2-2.6l1.8-2.4 l1.1,2.4l1.5,1.5L46,482.6z M43.4,516.1l3.7,0.8l3.7,1l0.8,1l-1.6,3.7l-3.1-0.2l-3.4-3.6L43.4,516.1z M22.7,502l1.1,2.6 l1.1,1.6l-1.1,0.8l-2.1-3.1V502H22.7z M9,575.1l3.4-2.3l3.4-1l2.6,0.3l0.5,1.6l1.9,0.5l1.9-1.9l-0.3-1.6l2.7-0.6l2.9,2.6 l-1.1,1.8l-4.4,1.1l-2.7-0.5l-3.7-1.1l-4.4,1.5l-1.6,0.3L9,575.1z M57.9,570.6l1.6,1.9l2.1-1.6l-1.5-1.3L57.9,570.6z M60.8,573.6l1.1-2.3l2.1,0.3l-0.8,1.9H60.8z M84.4,571.7l1.5,1.8l1-1.1l-0.8-1.9L84.4,571.7z M93.2,559.2l1.1,5.8l2.9,0.8 l5-2.9l4.4-2.6l-1.6-2.4l0.5-2.4l-2.1,1.3l-2.9-0.8l1.6-1.1l1.9,0.8l3.9-1.8l0.5-1.5l-2.4-0.8l0.8-1.9l-2.7,1.9l-4.7,3.6l-4.8,2.9L93.2,559.2z M135.5,539.4l2.4-1.5l-1-1.8l-1.8,1L135.5,539.4z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"AKn\" x=\"110\" y=\"504\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="AL"):
   statemapoutput = statemapoutput + "   <path id=\"AL\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M625.6,466.8l-1.6-15.2l-2.7-18.8l0.2-14.1l0.8-31l-0.2-16.7l0.2-6.4l7.8-0.4l27.8-2.6l8.9-0.7 l-0.1,2.2l0.2,2.1l0.6,3.4l3.4,7.9l2.4,9.9l1.5,6.1l1.6,4.8l1.5,7l2.1,6.3l2.6,3.4l0.5,3.4l1.9,0.8l0.2,2.1l-1.8,4.8l-0.5,3.2 l-0.2,1.9l1.6,4.4l0.3,5.3l-0.8,2.4l0.6,0.8l1.5,0.8l1,2.5h-6.3l-6.8,0.6l-25.5,2.9l-10.4,1.4l-0.1,3.8l1.8,1.8l2.6,1.9l0.6,7.9 l-5.5,2.6l-2.7-0.3l2.7-1.9v-1l-3.1-6l-2.3-0.6l-1.5,4.4l-1.3,2.7l-0.6-0.2H625.6z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"ALn\" x=\"641\" y=\"422\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="AR"):
   statemapoutput = statemapoutput + "   <path id=\"AR\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M591,345l-3.8,0.9l-6.2-0.5l0.7-3l3.2-2.7l0.5-2.3l-1.8-3l-11,0.5l-20.8,0.9l-23.3,0.7L505,337 l1.6,6.9v8.2l1.4,11l0.2,37.8l2.3,1.9l3-1.4l2.7,1.1l0.4,10.3l22.9-0.1l18.9-0.8l10.1-0.2l1.1-2.1l-0.3-3.5l-1.8-3l1.6-1.5 l-1.6-2.5l0.7-2.5l1.4-5.6l2.5-2.1l-0.7-2.3l3.7-5.4l2.7-1.4l-0.1-1.5l-0.3-1.8l2.9-5.6l2.4-1.3l0.4-3.4l1.8-1.2l0.9-4.2l-1.3-4 l4-2.4l0.6-2l1.2-4.3L591,345z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"ARn\" x=\"534\" y=\"384\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="AZ"):
   statemapoutput = statemapoutput + "   <path id=\"AZ\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M137.7,387.5l-2.6,2.2l-0.3,1.5l0.5,1l18.9,10.7l12.1,7.6l14.7,8.6l16.8,10l12.3,2.4l25.1,2.7 l2.5-12.5l3.8-27.2l7-52.9l4.3-31l-24.6-3.7l-27.2-4.6l-33.4-6.3l-2.9,18.1l-0.5,0.5l-1.7,2.6l-2.5-0.1l-1.3-2.7l-2.7-0.3l-0.9-1.1 h-0.9l-0.9,0.6l-1.9,1l-0.1,7l-0.2,1.7l-0.6,12.6l-1.5,2.2l-0.6,3.3l2.7,4.9l1.3,5.8l0.8,1l1,0.6l-0.1,2.3l-1.6,1.4l-3.4,1.7 l-1.9,1.9l-1.5,3.7l-0.6,4.9l-2.9,2.7l-2.1,0.7l-0.1,5.8l-0.5,1.7l0.5,0.8l3.7,0.6l-0.6,2.7l-1.5,2.2L137.7,387.5z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"AZn\" x=\"182\" y=\"368\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="CA"):
   statemapoutput = statemapoutput + "   <path id=\"CA\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M136.9,386.8l3.8-0.5l1.5-2l0.7-1.9l-3.2-0.1l-1.1-1.8l0.8-1.7l0-6.2l2.2-1.3l2.7-2.6l0.4-4.9 l1.6-3.5l1.9-2.1l3.3-1.7l1.3-0.7l0.8-1.5l-0.9-0.9l-1-1.5l-0.9-5.3l-2.9-5.2l0.1-2.8l-2.2-3.2l-15-23.2l-19.4-28.7l-22.4-33 l-12.7-19.5l1.8-7.2l6.8-25.9l8.1-31.4l-12.4-3.3l-13.5-3.4l-12.6-4.1l-7.5-2.1l-11.4-3l-7.1-2.4l-1.6,4.7l-0.2,7.4l-5.2,11.8 l-3.1,2.6l-0.3,1.1l-1.8,0.8l-1.5,4.2l-0.8,3.2l2.7,4.2l1.6,4.2l1.1,3.6l-0.3,6.5l-1.8,3.1l-0.6,5.8l-1,3.7l1.8,3.9l2.7,4.5 l2.3,4.8l1.3,4l-0.3,3.2l-0.3,0.5v2.1l5.7,6.3l-0.5,2.4l-0.6,2.3l-0.6,1.9l0.2,8.2l2.1,3.7l1.9,2.6l2.7,0.5l1,2.7l-1.1,3.6 l-2.1,1.6h-1.1l-0.8,3.9l0.5,2.9l3.2,4.4l1.6,5.3l1.5,4.7l1.3,3.1l3.4,5.8l1.5,2.6l0.5,2.9l1.6,1v2.4l-0.8,1.9l-1.8,7.1l-0.5,1.9 l2.4,2.7l4.2,0.5l4.5,1.8l3.9,2.1h2.9l2.9,3.1l2.6,4.8l1.1,2.3l3.9,2.1l4.8,0.8l1.5,2.1l0.6,3.2l-1.5,0.6l0.3,1l3.2,0.8l2.7,0.2 l2.9,4.7l3.9,4.2l0.8,2.3l2.6,4.2l0.3,3.2v9.4l0.5,1.8l10,1.5l19.7,2.7L136.9,386.8z M48.8,337l1.3,1.5l-0.2,1.3l-3.2-0.1 l-0.6-1.2l-0.6-1.5L48.8,337z M50.7,337l1.2-0.6l3.6,2.1l3.1,1.2l-0.9,0.6l-4.5-0.2l-1.6-1.6L50.7,337z M71.4,356.8l1.8,2.3 l0.8,1l1.5,0.6l0.6-1.5l-1-1.8l-2.7-2l-1.1,0.2V356.8z M70,365.5l1.8,3.2l1.2,1.9l-1.5,0.2l-1.3-1.2c0,0-0.7-1.5-0.7-1.9 s0-2.2,0-2.2L70,365.5z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"CAn\" x=\"55\" y=\"298\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="CO"):
   statemapoutput = statemapoutput + "   <path id=\"CO\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M378.6,256.8l1.4-21.3l-32.1-3.1l-24.5-2.7l-37.3-4.1l-20.7-2.5l-2.6,22.2l-3.2,22.4l-3.8,28 l-1.5,11.1l-0.3,2.8l33.9,3.8l37.7,4.3l32,3.2l16.6,0.8\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"COn\" x=\"311\" y=\"283\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="CT"):
   statemapoutput = statemapoutput + "   <path id=\"CT\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M873.2,180.1l-0.6-4.2l-0.8-4.4l-1.6-6l-4.2,0.9l-21.8,4.8l0.6,3.3l1.5,7.3v8.1l-1.1,2.3l1.8,2.1 l5-3.4l3.6-3.2l1.9-2.1l0.8,0.6l2.7-1.5l5.2-1.1L873.2,180.1z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"CTn\" x=\"918\" y=\"228\" font-size=\"22\">CT "+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="DC"):
   statemapoutput_dclast = "   <path id=\"DC\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" stroke=\"#FFFFFF\" d=\"M 807,260l-6.26,-3.18l-5.97,3.60l1.09,-6.93l-5.27,-4.56l6.93,-1.11l2.71,-6.42l3.19,6.25dclast0.59l-4.96,4.97 L 807,260 z\"/>\n"
   statetextoutput_dclast = "   <text id=\"DCn\" x=\"864\" y=\"327\" font-size=\"22\">DC "+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="DE"):
   statemapoutput = statemapoutput + "   <path id=\"DE\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M822.4,230.4l0.6-2.1l0-1.2l-1.3-0.1l-2.1,1.6l-1.5,1.5l1.5,4.2l2.3,5.7l2.1,9.7l1.6,6.3l5-0.2 l6.1-1.2l-2.3-7.4l-1,0.5l-3.6-2.4l-1.8-4.7l-1.9-3.6l-2.3-1l-2.1-3.6L822.4,230.4z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"DEn\" x=\"891\" y=\"284\" font-size=\"22\">DE "+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="FL"):
   statemapoutput = statemapoutput + "   <path id=\"FL\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M755.4,445.5l2.3,7.3l3.7,9.7l5.3,9.4l3.7,6.3l4.8,5.5l4,3.7l1.6,2.9l-1.1,1.3L779,493l2.9,7.4 l2.9,2.9l2.6,5.3l3.6,5.8l4.5,8.2l1.3,7.6l0.5,12l0.6,1.8l-0.3,3.4l-2.4,1.3l0.3,1.9l-0.6,1.9l0.3,2.4l0.5,1.9l-2.7,3.2l-3.1,1.5 l-3.9,0.2l-1.5,1.6l-2.4,1l-1.3-0.5l-1.1-1l-0.3-2.9l-0.8-3.4l-3.4-5.2l-3.6-2.3l-3.9-0.3l-0.8,1.3l-3.1-4.4l-0.6-3.6l-2.6-4 l-1.8-1.1l-1.6,2.1l-1.8-0.3l-2.1-5l-2.9-3.9l-2.9-5.3l-2.6-3.1l-3.6-3.7l2.1-2.4l3.2-5.5l-0.2-1.6l-4.5-1l-1.6,0.6l0.3,0.6l2.6,1 l-1.5,4.5l-0.8,0.5l-1.8-4l-1.3-4.8l-0.3-2.7l1.5-4.7v-9.5L736,485l-1.3-3.1l-5.2-1.3l-1.9-0.6l-1.6-2.6l-3.4-1.6l-1.1-3.4l-2.7-1 l-2.4-3.7l-4.2-1.5l-2.9-1.5h-2.6l-4,0.8l-0.2,1.9l0.8,1l-0.5,1.1l-3.1-0.2l-3.7,3.6l-3.6,1.9h-3.9l-3.2,1.3l-0.3-2.7l-1.6-1.9 l-2.9-1.1l-1.6-1.5l-8.1-3.9l-7.6-1.8l-4.4,0.6l-6,0.5l-6,2.1l-3.5,0.6l-0.2-8l-2.6-1.9l-1.8-1.8l0.3-3.1l10.2-1.3l25.5-2.9 l6.8-0.6l5.4,0.3l2.6,3.9l1.5,1.5l8.1,0.5l10.8-0.6l21.5-1.3l5.4-0.7l4.6,0l0.2,2.9l3.8,0.8l0.3-4.8l-1.6-4.5l1-0.7l5.1,0.5 L755.4,445.5z M767.9,577.9l2.4-0.6l1.3-0.2l1.5-2.3l2.3-1.6l1.3,0.5l1.7,0.3l0.4,1.1l-3.5,1.2l-4.2,1.5l-2.3,1.2L767.9,577.9z M781.4,572.9l1.2,1.1l2.7-2.1l5.3-4.2l3.7-3.9l2.5-6.6l1-1.7l0.2-3.4l-0.7,0.5l-1,2.8l-1.5,4.6l-3.2,5.3l-4.4,4.2l-3.4,1.9 L781.4,572.9z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"FLn\" x=\"743\" y=\"505\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="GA"):
   statemapoutput = statemapoutput + "   <path id=\"GA\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M689.6,358l-4.8,0.8l-8.4,1.1l-8.6,0.9v2.2l0.2,2.1l0.6,3.4l3.4,7.9l2.4,9.9l1.5,6.1l1.6,4.8l1.5,7 l2.1,6.3l2.6,3.4l0.5,3.4l1.9,0.8l0.2,2.1l-1.8,4.8l-0.5,3.2l-0.2,1.9l1.6,4.4l0.3,5.3l-0.8,2.4l0.6,0.8l1.5,0.8l0.6,3.4l2.6,3.9 l1.5,1.5l7.9,0.2l10.8-0.6l21.5-1.3l5.4-0.7l4.6,0l0.2,2.9l2.6,0.8l0.3-4.4l-1.6-4.5l1.1-1.6l5.8,0.8l5,0.3l-0.8-6.3l2.3-10 l1.5-4.2l-0.5-2.6l3.3-6.2l-0.5-1.4l-1.9,0.7l-2.6-1.3l-0.6-2.1l-1.3-3.6l-2.3-2.1l-2.6-0.6l-1.6-4.8l-2.9-6.3l-4.2-1.9l-2.1-1.9 l-1.3-2.6l-2.1-1.9l-2.3-1.3l-2.3-2.9l-3.1-2.3l-4.5-1.8l-0.5-1.5l-2.4-2.9l-0.5-1.5l-3.4-4.9l-3.4,0.2l-4.1-3l-1.3-1.3l-0.3-1.8 l0.8-1.9l2.4-1.2l-1.1-1.2l0.1-0.3l-5.8,1l-7,0.8L689.6,358z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"GAn\" x=\"697\" y=\"419\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="HI"):
   statemapoutput = statemapoutput + "   <path id=\"HI\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M233.1,519.3l1.9-3.6l2.3-0.3l0.3,0.8l-2.1,3.1H233.1z M243.3,515.6l6.1,2.6l2.1-0.3l1.6-3.9 l-0.6-3.4l-4.2-0.5l-4,1.8L243.3,515.6z M274,525.6l3.7,5.5l2.4-0.3l1.1-0.5l1.5,1.3l3.7-0.2l1-1.5l-2.9-1.8l-1.9-3.7l-2.1-3.6 l-5.8,2.9L274,525.6z M294.2,534.5l1.3-1.9l4.7,1l0.6-0.5l6.1,0.6l-0.3,1.3l-2.6,1.5l-4.4-0.3L294.2,534.5z M299.5,539.7l1.9,3.9 l3.1-1.1l0.3-1.6l-1.6-2.1l-3.7-0.3V539.7z M306.5,538.5l2.3-2.9l4.7,2.4l4.4,1.1l4.4,2.7v1.9l-3.6,1.8l-4.8,1l-2.4-1.5 L306.5,538.5z M323.1,554.1l1.6-1.3l3.4,1.6l7.6,3.6l3.4,2.1l1.6,2.4l1.9,4.4l4,2.6l-0.3,1.3l-3.9,3.2l-4.2,1.5l-1.5-0.6l-3.1,1.8 l-2.4,3.2l-2.3,2.9l-1.8-0.2l-3.6-2.6l-0.3-4.5l0.6-2.4l-1.6-5.7l-2.1-1.8l-0.2-2.6l2.3-1l2.1-3.1l0.5-1l-1.6-1.8L323.1,554.1z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"HIn\" x=\"261\" y=\"565\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="IA"):
   statemapoutput = statemapoutput + "   <path id=\"IA\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M566.6,201.6l0.2,1.9l2.3,1.1l1.1,1.3l0.3,1.3l3.9,3.2l0.7,2.2l-0.8,2.9l-1.5,3.5l-0.8,2.7 l-2.2,1.6l-1.7,0.6l-5.5,1.5l-0.7,2.3l-0.8,2.3l0.6,1.4l1.7,1.7l0,3.7l-2.2,1.6l-0.5,1.5v2.5l-1.5,0.5l-1.7,1.4l-0.5,1.5l0.5,1.7 l-1.4,1.2l-2.3-2.9l-1.5-2.6l-8.3,0.8l-10.2,0.6l-25,0.7l-13,0.2l-9.4,0.2l-1.3,0.1l-1.7-4.5l-0.2-6.6l-1.6-4.1l-0.7-5.3l-2.3-3.7 l-0.9-4.8l-2.7-7.5l-1.1-5.4l-1.4-2.2l-1.6-2.7l1.8-4.3l1.4-5.7l-2.7-2.1l-0.5-2.7l0.9-2.5h1.7h11.5l49.6-0.7l19.9-0.7l1.9,2.7 l1.8,2.6l0.5,0.8l-1.8,2.7l0.5,4.2l2.5,3.9l3,1.8l2.4,0.2L566.6,201.6z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"IAn\" x=\"513\" y=\"224\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="ID"):
   statemapoutput = statemapoutput + "   <path id=\"ID\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M162.1,181c-22.6-4.3-14.1-2.8-21.1-4.4l4.4-17.5l4.3-17.7l1.4-4.2l2.5-5.9l-1.3-2.3l-2.5,0.1 l-0.8-1l0.5-1.1l0.3-3.1l4.5-5.5l1.8-0.5l1.1-1.1l0.6-3.2l0.9-0.7l3.9-5.8l3.9-4.3l0.2-3.8l-3.4-2.6l-1.3-4.4l0.4-9.7l3.7-16.5 l4.5-20.8l3.8-13.5l0.8-3.8l13,2.5l-4.2,21.5l2.9,7.7l-1.1,4.6l2,4.6l3.2,1.7l4.5,9.8l2.7,3.8l0.6,1.1l3.4,1.1l0.5,2.5l-6.9,16.8 l0.3,3.3l2.7,2.9l1.9,0.5l4.8-3.6l0.4-0.5l0.2,0.8l0.3,4.1l2.6,12.9l3.5,2.7l0.4,0.8l2.1,2.4l-0.8,2.8l0.7,3.8l1.9,0.9l2.1-1.6 l2.6-0.5l3.4,1.6l2.5-0.6l3.8-0.2l4,1.6l2.7-0.3l0.9-2.3l2.5-1.6l0.7,1.7l0.6,2.2l2.3,2.5l-3.8,24l-5.1,29l-4.2-0.3l-8.2-1.5 l-9.8-1.8l-12.2-2.4l-12.5-2.5l-8.5-1.8l-9.3-1.7L162.1,181z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"IDn\" x=\"183\" y=\"162\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="IL"):
   statemapoutput = statemapoutput + "   <path id=\"IL\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M617.8,301.5v-3.6l0.3-4.9l2.4-3.1l1.8-3.8l2.6-3.9l-0.4-5.3l-2-3.5l-0.1-3.3l0.7-5.3l-0.8-7.2 l-1.1-15.8l-1.3-15l-0.9-11.6l-0.3-0.9l-0.8-2.6l-1.3-3.7l-1.6-1.8l-1.5-2.6l-0.2-5.5l-9.9,1.3l-27.2,1.7l-8.7-0.4l0.2,2.4l2.3,0.7 l0.9,1.1l0.5,1.8l3.9,3.4l0.7,2.3l-0.7,3.4l-1.8,3.7l-0.7,2.5l-2.3,1.8l-1.8,0.7l-5.3,1.4l-0.7,1.8L562,230l0.7,1.4l1.8,1.6 l-0.2,4.1l-1.8,1.6l-0.7,1.6v2.7l-1.8,0.5l-1.6,1.1l-0.2,1.4l0.2,2.1l-1.7,1.3l-1,2.8l0.5,3.7l2.3,7.3l7.3,7.5l5.5,3.7l-0.2,4.3 l0.9,1.4l6.4,0.5l2.7,1.4l-0.7,3.7l-2.3,5.9l-0.7,3.2l2.3,3.9l6.4,5.3l4.6,0.7l2.1,5l2.1,3.2l-0.9,3l1.6,4.1l1.8,2.1l1.9-0.8 l0.7-2.2l2-1.4l3.2-1.1l3.1,1.2l2.9,1.1l0.8-0.2l-0.1-1.2l-1.1-2.8l0.4-2.4l2.3-1.6l2.4-1l1.2-0.4l-0.6-1.3l-0.8-2.2l1.2-1.3 L617.8,301.5z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"ILn\" x=\"579\" y=\"261\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="IN"):
   statemapoutput = statemapoutput + "   <path id=\"IN\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M618.4,300.9l0.1-2.9l0.5-4.5l2.3-2.9l1.8-3.9l2.6-4.2l-0.5-5.8l-1.8-2.7l-0.3-3.2l0.8-5.5l-0.5-7 l-1.3-16l-1.3-15.4l-1-11.7l3.1,0.9l1.5,1l1.1-0.3l2.1-1.9l2.8-1.6l5.1-0.2l22-2.3l5.6-0.5l1.5,16l4.3,36.8l0.6,5.8L669,271 l1.2,1.8l0.1,1.4l-2.5,1.6l-3.5,1.6l-3.2,0.6l-0.6,4.9l-4.6,3.3l-2.8,4l0.3,2.4l-0.6,1.5h-3.3l-1.6-1.6l-2.5,1.3l-2.7,1.5l0.2,3.1 l-1.2,0.3l-0.5-1l-2.2-1.5l-3.3,1.3l-1.6,3l-1.4-0.8l-1.5-1.6l-4.5,0.5l-5.6,1L618.4,300.9z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"INn\" x=\"630\" y=\"262\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="KS"):
   statemapoutput = statemapoutput + "   <path id=\"KS\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M503.4,325.1l-12.6,0.2l-46.1-0.5l-44.6-2.1l-24.6-1.3l4.1-64.7l21.8,0.8l40.5,1.4l44.1,0.5h5.1 l3.2,3.2l2.8,0.2l0.9,1.1v2l-1.8,1.6l-0.5,2.6l2.2,3.6l2.5,3.1l2.5,2l1.1,11.2L503.4,325.1z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"KSn\" x=\"434\" y=\"303\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="KY"):
   statemapoutput = statemapoutput + "   <path id=\"KY\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M721.8,297.8l-2.3,2.7l-4.2,3.6L711,310l-1.8,1.8v2.1l-3.9,2.1l-5.7,3.4l-3.5,0.4l-51.9,4.9 l-15.8,1.8l-4.6,0.5l-3.9,0l-0.2,4.2l-8.2,0.1l-7,0.6l-10.4,0.2l1.9-0.2l2.2-1.8l2.1-1.1l0.2-3.2l0.9-1.8l-1.6-2.5l0.8-1.9l2.3-1.8 l2.1-0.6l2.7,1.3l3.6,1.3l1.1-0.3l0.2-2.3l-1.3-2.4l0.3-2.3l1.9-1.5l2.6-0.6l1.6-0.6l-0.8-1.8l-0.6-1.9l1.1-0.8l1.1-3.3l3-1.7 l5.8-1l3.6-0.5l1.5,1.9l1.8,0.8l1.8-3.2l2.9-1.5l1.9,1.6l0.8,1.1l2.1-0.5l-0.2-3.4l2.9-1.6l1.1-0.8l1.1,1.6h4.7l0.8-2.1l-0.3-2.3 l2.9-3.6l4.7-3.9l0.5-4.5l2.7-0.3l3.9-1.8l2.7-1.9l-0.3-1.9l-1.5-1.5l0.6-2.2l4.1-0.2l2.4-0.8l2.9,1.6l1.6,4.4l5.8,0.3l1.8,1.8 l2.1,0.2l2.4-1.5l3.1,0.5l1.3,1.5l2.7-2.6l1.8-1.3h1.6l0.6,2.7l1.8,1l2.4,2.2l0.2,5.5l0.8,1.6l2.6,1.5l0.6,2.3l2.9,3.7l2.6,2.7 L721.8,297.8z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"KYn\" x=\"666\" y=\"311\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="LA"):
   statemapoutput = statemapoutput + "   <path id=\"LA\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M602.2,473l-1-2.6l-1.1-3.1l-3.3-3.5l0.9-6.8l-0.1-1.1l-1.3,0.3l-8.2,0.9l-25,0.5l-0.7-2.4l0.9-8.5 l3.3-5.9l5-8.7l-0.6-2.4l1.3-0.7l0.5-2l-2.3-2.1l-0.1-1.9l-1.8-4.3l-0.5-5.9l-9.7,0.1l-19.2,0.9l-22.2,0l0,9.6l0.7,9.4l0.7,3.9 l2.5,4.1l0.9,5l4.3,5.5l0.2,3.2l0.7,0.7l-0.7,8.5l-3,5l1.6,2.1l-0.7,2.5l-0.7,7.3l-1.4,3.2l0.1,3.6l4.7-1.5l8.1-0.3l10.3,3.6 l6.5,1.1l3.7-1.5l3.2,1.1l3.2,1l0.8-2.1l-3.2-1.1l-2.6,0.5l-2.7-1.6c0,0,0.2-1.3,0.8-1.5c0.6-0.2,3.1-1,3.1-1l1.8,1.5l1.8-1 l3.2,0.6l1.5,2.4l0.3,2.3l4.5,0.3l1.8,1.8l-0.8,1.6l-1.3,0.8l1.6,1.6l8.4,3.6l3.6-1.3l1-2.4l2.6-0.6l1.8-1.5l1.3,1l0.8,2.9 l-2.3,0.8l0.6,0.6l3.4-1.3l2.3-3.4l0.8-0.5l-2.1-0.3l0.8-1.6l-0.2-1.5l2.1-0.5l1.1-1.3l0.6,0.8c0,0-0.2,3.1,0.6,3.1 c0.8,0,4.2,0.6,4.2,0.6l4,1.9l1,1.5h2.9l1.1,1l2.3-3.1v-1.5h-1.3l-3.4-2.7l-5.8-0.8l-3.2-2.3l1.1-2.7l2.3,0.3l0.2-0.6l-1.8-1v-0.5 h3.2l1.8-3.1l-1.3-1.9l-0.3-2.7l-1.5,0.2l-1.9,2.1l-0.6,2.6l-3.1-0.6l-1-1.8l1.8-1.9l2-1.8L602.2,473z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"LAn\" x=\"536\" y=\"452\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="MA"):
   statemapoutput = statemapoutput + "   <path id=\"MA\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M900,173.9l2.2-0.7l0.5-1.7l1,0.1l1,2.3l-1.3,0.5l-3.9,0.1L900,173.9z M890.6,174.7l2.3-2.6h1.6 l1.8,1.5l-2.4,1l-2.2,1L890.6,174.7z M855.8,152.7l17.5-4.2l2.3-0.6l2.1-3.2l3.7-1.7l2.9,4.4l-2.4,5.2l-0.3,1.5l1.9,2.6l1.1-0.8 h1.8l2.3,2.6l3.9,6l3.6,0.5l2.3-1l1.8-1.8l-0.8-2.7l-2.1-1.6l-1.5,0.8l-1-1.3l0.5-0.5l2.1-0.2l1.8,0.8l1.9,2.4l1,2.9l0.3,2.4 l-4.2,1.5l-3.9,1.9l-3.9,4.5l-1.9,1.5v-1l2.4-1.5l0.5-1.8l-0.8-3.1l-2.9,1.5l-0.8,1.5l0.5,2.3l-2.1,1l-2.7-4.5l-3.4-4.4l-2.1-1.8 l-6.5,1.9l-5.1,1.1l-21.8,4.8l-0.4-4.9l0.6-10.6l5.2-0.9L855.8,152.7z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"MAn\" x=\"927\" y=\"164\" font-size=\"22\">MA "+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="MD"):
   statemapoutput = statemapoutput + "   <path id=\"MD\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M837,255.3l-6.1,1.3l-5.8,0.2l-1.8-7.1l-2.1-9.7l-2.3-5.7l-1.3-4.4l-7.5,1.6l-14.9,2.8l-37.5,7.6 l1.1,5l1,5.7l0.3-0.3l2.1-2.4l2.3-2.6l2.4-0.6l1.5-1.5l1.8-2.6l1.3,0.6l2.9-0.3l2.6-2.1l2-1.5l1.8-0.5l1.6,1.1l2.9,1.5l1.9,1.8 l1.2,1.5l4.1,1.7v2.9l5.5,1.3l1.1,0.5l1.4-2l2.9,2l-1.3,2.5l-0.8,4l-1.8,2.6v2.1l0.6,1.8l5.1,1.4l4.3-0.1l3.1,1l2.1,0.3l1-2.1 l-1.5-2.1v-1.8l-2.4-2.1l-2.1-5.5l1.3-5.3l-0.2-2.1l-1.3-1.3c0,0,1.5-1.6,1.5-2.3c0-0.6,0.5-2.1,0.5-2.1l1.9-1.3l1.9-1.6l0.5,1 l-1.5,1.6l-1.3,3.7l0.3,1.1l1.8,0.3l0.5,5.5l-2.1,1l0.3,3.6l0.5-0.2l1.1-1.9l1.6,1.8l-1.6,1.3l-0.3,3.4l2.6,3.4l3.9,0.5l1.6-0.8 l3.2,4.2l1.4,0.5l6.7-2.8l2-4L837,255.3z M820.3,264.3l1.1,2.5l0.2,1.8l1.1,1.9c0,0,0.9-0.9,0.9-1.2c0-0.3-0.7-3.1-0.7-3.1 l-0.7-2.3L820.3,264.3z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"MDn\" x=\"883\" y=\"305\" font-size=\"22\">MD "+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="ME"):
   if(winning_candidate_states_split[il]!=winning_candidate_states_split[il+1]):
    statemapoutput = statemapoutput + "   <path id=\"ME\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M923.2,77.3l1.9,2.1l2.3,3.7v1.9l-2.1,4.7l-1.9,0.6l-3.4,3.1l-4.8,5.5c0,0-0.6,0-1.3,0 c-0.6,0-1-2.1-1-2.1l-1.8,0.2l-1,1.5l-2.4,1.5l-1,1.5l1.6,1.5l-0.5,0.6l-0.5,2.7l-1.9-0.2v-1.6l-0.3-1.3l-1.5,0.3l-1.8-3.2 l-2.1,1.3l1.3,1.5l0.3,1.1l-0.8,1.3l0.3,3.1l0.2,1.6l-1.6,2.6l-2.9,0.5l-0.3,2.9l-5.3,3.1l-1.3,0.5l-1.6-1.5l-3.1,3.6l1,3.2 l-1.5,1.3l-0.2,4.4l-1.1,6.3l-2.5-1.2l-0.5-3.1l-3.9-1.1l-0.3-2.7l-7.3-23.4l-4.2-13.6l1.4-0.1l1.5,0.4v-2.6l0.8-5.5l2.6-4.7l1.5-4 l-1.9-2.4v-6l0.8-1l0.8-2.7l-0.2-1.5l-0.2-4.8l1.8-4.8l2.9-8.9l2.1-4.2h1.3l1.3,0.2v1.1l1.3,2.3l2.7,0.6l0.8-0.8v-1l4-2.9l1.8-1.8 l1.5,0.2l6,2.4l1.9,1l9.1,29.9h6l0.8,1.9l0.2,4.8l2.9,2.3h0.8l0.2-0.5l-0.5-1.1L923.2,77.3z M902.3,107.5l1.5-1.5l1.4,1.1 l0.6,2.4l-1.7,0.9L902.3,107.5z M909,101.6l1.8,1.9c0,0,1.3,0.1,1.3-0.2s0.2-2,0.2-2l0.9-0.8l-0.8-1.8l-2,0.7L909,101.6z\"/>\n"
    statetextoutput = statetextoutput + "   <text id=\"MEn\" x=\"884\" y=\"74\">"+str(electoral_college_points_split[il])+"</text>\n";
    candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
   if(winning_candidate_states_split[il]==winning_candidate_states_split[il+1]):
    statemapoutput = statemapoutput + "   <path id=\"ME\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M923.2,77.3l1.9,2.1l2.3,3.7v1.9l-2.1,4.7l-1.9,0.6l-3.4,3.1l-4.8,5.5c0,0-0.6,0-1.3,0 c-0.6,0-1-2.1-1-2.1l-1.8,0.2l-1,1.5l-2.4,1.5l-1,1.5l1.6,1.5l-0.5,0.6l-0.5,2.7l-1.9-0.2v-1.6l-0.3-1.3l-1.5,0.3l-1.8-3.2 l-2.1,1.3l1.3,1.5l0.3,1.1l-0.8,1.3l0.3,3.1l0.2,1.6l-1.6,2.6l-2.9,0.5l-0.3,2.9l-5.3,3.1l-1.3,0.5l-1.6-1.5l-3.1,3.6l1,3.2 l-1.5,1.3l-0.2,4.4l-1.1,6.3l-2.5-1.2l-0.5-3.1l-3.9-1.1l-0.3-2.7l-7.3-23.4l-4.2-13.6l1.4-0.1l1.5,0.4v-2.6l0.8-5.5l2.6-4.7l1.5-4 l-1.9-2.4v-6l0.8-1l0.8-2.7l-0.2-1.5l-0.2-4.8l1.8-4.8l2.9-8.9l2.1-4.2h1.3l1.3,0.2v1.1l1.3,2.3l2.7,0.6l0.8-0.8v-1l4-2.9l1.8-1.8 l1.5,0.2l6,2.4l1.9,1l9.1,29.9h6l0.8,1.9l0.2,4.8l2.9,2.3h0.8l0.2-0.5l-0.5-1.1L923.2,77.3z M902.3,107.5l1.5-1.5l1.4,1.1 l0.6,2.4l-1.7,0.9L902.3,107.5z M909,101.6l1.8,1.9c0,0,1.3,0.1,1.3-0.2s0.2-2,0.2-2l0.9-0.8l-0.8-1.8l-2,0.7L909,101.6z\"/>\n"
    statetextoutput = statetextoutput + "   <text id=\"MEn\" x=\"884\" y=\"74\">"+str(electoral_college_points_split[il] + 1)+"</text>\n";
    candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il] + 1;
  if(state_initials_split[il]=="ME-2"):
   if(winning_candidate_states_split[il]!=winning_candidate_states_split[il-1]):
    statemapoutput = statemapoutput + "<circle id=\"ME-2\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" cx=\"884\" cy=\"96\" r=\"14\"/>\n"
    statetextoutput = statetextoutput + "   <text id=\"ME-2n\" x=\"877\" y=\"104\" font-size=\"25\">"+str(electoral_college_points_split[il])+"</text>\n";
    candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="MI"):
   statemapoutput = statemapoutput + "   <path id=\"MI\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M581.6,82.1l1.8-2.1l2.2-0.8l5.4-3.9l2.3-0.6l0.5,0.5l-5.1,5.1l-3.3,1.9l-2.1,0.9L581.6,82.1z M667.8,114.2l0.6,2.5l3.2,0.2l1.3-1.2c0,0-0.1-1.5-0.4-1.6c-0.3-0.2-1.6-1.9-1.6-1.9l-2.2,0.2l-1.6,0.2l-0.3,1.1L667.8,114.2z M697.9,177.2l-3.2-8.2l-2.3-9.1l-2.4-3.2l-2.6-1.8l-1.6,1.1l-3.9,1.8l-1.9,5l-2.7,3.7l-1.1,0.6l-1.5-0.6c0,0-2.6-1.5-2.4-2.1 c0.2-0.6,0.5-5,0.5-5l3.4-1.3l0.8-3.4l0.6-2.6l2.4-1.6l-0.3-10l-1.6-2.3l-1.3-0.8l-0.8-2.1l0.8-0.8l1.6,0.3l0.2-1.6L676,131 l-1.3-2.6h-2.6l-4.5-1.5l-5.5-3.4h-2.7l-0.6,0.6l-1-0.5l-3.1-2.3l-2.9,1.8l-2.9,2.3l0.3,3.6l1,0.3l2.1,0.5l0.5,0.8l-2.6,0.8 l-2.6,0.3l-1.5,1.8l-0.3,2.1l0.3,1.6l0.3,5.5l-3.6,2.1l-0.6-0.2v-4.2l1.3-2.4l0.6-2.4l-0.8-0.8l-1.9,0.8l-1,4.2l-2.7,1.1l-1.8,1.9 l-0.2,1l0.6,0.8l-0.6,2.6l-2.3,0.5v1.1l0.8,2.4l-1.1,6.1l-1.6,4l0.6,4.7l0.5,1.1l-0.8,2.4l-0.3,0.8l-0.3,2.7l3.6,6l2.9,6.5l1.5,4.8 l-0.8,4.7l-1,6l-2.4,5.2l-0.3,2.7l-3.3,3.1l4.4-0.2l21.4-2.3l7.3-1l0.1,1.7l6.9-1.2l10.3-1.5l3.9-0.5l0.1-0.6l0.2-1.5l2.1-3.7 l2-1.7l-0.2-5.1l1.6-1.6l1.1-0.3l0.2-3.6l1.5-3l1.1,0.6l0.2,0.6l0.8,0.2l1.9-1L697.9,177.2z M567.5,111.2l0.7-0.6l2.7-0.8l3.6-2.3 v-1l0.6-0.6l6-1l2.4-1.9l4.4-2.1l0.2-1.3l1.9-2.9l1.8-0.8l1.3-1.8l2.3-2.3l4.4-2.4l4.7-0.5l1.1,1.1l-0.3,1l-3.7,1l-1.5,3.1 l-2.3,0.8l-0.5,2.4l-2.4,3.2l-0.3,2.6l0.8,0.5l1-1.1l3.6-2.9l1.3,1.3h2.3l3.2,1l1.5,1.1l1.5,3.1l2.7,2.7l3.9-0.2l1.5-1l1.6,1.3 l1.6,0.5l1.3-0.8h1.1l1.6-1l4-3.6l3.4-1.1l6.6-0.3l4.5-1.9l2.6-1.3l1.5,0.2v5.7l0.5,0.3l2.9,0.8l1.9-0.5l6.1-1.6l1.1-1.1l1.5,0.5v7 l3.2,3.1l1.3,0.6l1.3,1l-1.3,0.3l-0.8-0.3l-3.7-0.5l-2.1,0.6l-2.3-0.2l-3.2,1.5h-1.8l-5.8-1.3l-5.2,0.2l-1.9,2.6l-7,0.6l-2.4,0.8 l-1.1,3.1l-1.3,1.1l-0.5-0.2l-1.5-1.6l-4.5,2.4h-0.6l-1.1-1.6l-0.8,0.2l-1.9,4.4l-1,4l-3.2,7l-1.2-1l-1.4-1l-1.9-10.3l-3.5-1.4 l-2.1-2.3l-12.1-2.7l-2.9-1l-8.2-2.2l-7.9-1.1L567.5,111.2z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"MIn\" x=\"645\" y=\"193\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="MN"):
   statemapoutput = statemapoutput + "   <path id=\"MN\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M471.9,128.5l-0.5-8.5l-1.8-7.3l-1.8-13.5l-0.5-9.8l-1.8-3.4l-1.6-5v-10.3l0.7-3.9l-1.8-5.5l30.1,0 l0.3-8.2l0.6-0.2l2.3,0.5l1.9,0.8l0.8,5.5l1.5,6.1l1.6,1.6h4.8l0.3,1.5l6.3,0.3v2.1h4.8l0.3-1.3l1.1-1.1l2.3-0.6l1.3,1h2.9l3.9,2.6 l5.3,2.4l2.4,0.5l0.5-1l1.5-0.5l0.5,2.9l2.6,1.3l0.5-0.5l1.3,0.2v2.1l2.6,1h3.1l1.6-0.8l3.2-3.2l2.6-0.5l0.8,1.8l0.5,1.3h1l1-0.8 l8.9-0.3l1.8,3.1h0.6l0.7-1.1l4.4-0.4l-0.6,2.3l-3.9,1.8l-9.2,4.1l-4.8,2l-3.1,2.6l-2.4,3.6l-2.3,3.9l-1.8,0.8l-4.5,5l-1.3,0.2 l-3.8,2.9l-2.8,3.2l-0.2,3l0.2,7.8l-1.6,1.6L530,128l-1.8,5.7l2.5,3.6l0.5,2.5l-1.1,3l-0.2,3.7l0.5,7.1l3.4,4.1h3l2.5,2.3l3.2,1.4 l3.7,5l7.1,5l1.8,2.1l0.2,5.7l-20.6,0.7l-60.2,0.5l-0.3-35.7l-0.5-3l-4.1-3.4l-1.1-1.8v-1.6l2.1-1.6l1.4-1.4L471.9,128.5z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"MNn\" x=\"484\" y=\"129\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="MO"):
   statemapoutput = statemapoutput + "   <path id=\"MO\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M555.8,249.5l-2.5-3.1l-1.1-2.3l-7.8,0.7l-9.8,0.5l-25.4,0.9l-13.5,0.2l-7.9,0.1l-2.3,0.1l1.3,2.5 l-0.2,2.3l2.5,3.9l3.1,4.1l3.1,2.7l2.3,0.2l1.4,0.9v3l-1.8,1.6l-0.5,2.3l2.1,3.4l2.5,3l2.5,1.8l1.4,11.7l-0.7,35.3l0.2,4.7l0.5,5.4 l23.4-0.1l23.2-0.7l20.8-0.8l11.7-0.2l2.2,3.4l-0.7,3.3l-3.1,2.4l-0.6,1.8l5.4,0.5l3.9-0.7l1.7-5.5l0.7-5.9l2.3-2l1.7-1.5l2.1-1 l0.1-2.9l0.6-1.7l-1-1.7l-2.7,0.1l-2.2-2.6l-1.4-4.2l0.8-2.5l-1.9-3.4l-1.8-4.6l-4.8-0.8l-7-5.6l-1.7-4.1l0.8-3.2l2.1-6.1l0.5-2.9 l-1.9-1l-6.9-0.8l-1-1.7l-0.1-4.2l-5.5-3.4l-7-7.8l-2.3-7.3l-0.2-4.2L555.8,249.5z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"MOn\" x=\"525\" y=\"306\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="MS"):
   statemapoutput = statemapoutput + "   <path id=\"MS\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M624.6,467l-0.3,1.3h-5.2l-1.5-0.8l-2.1-0.3l-6.8,1.9l-1.8-0.8l-2.6,4.2l-1.1,0.8l-1.1-2.5 l-1.1-3.9l-3.4-3.2l1.1-7.5l-0.7-0.9l-1.8,0.2l-8.2,0.7l-24.2,0.7l-0.5-1.6l0.7-8l3.4-6.2l5.3-9.1l-0.9-2.1h1.1l0.7-3.2l-2.3-1.8 l0.2-1.8l-2.1-4.6l-0.3-5.3l1.4-2.7l-0.4-4.3l-1.4-3l1.4-1.4l-1.4-2.1l0.5-1.8l0.9-6.2l3-2.7l-0.7-2.1l3.7-5.3l2.7-0.9v-2.5 l-0.7-1.4l2.7-5.3l2.7-1.1l0.1-3.4l8.7-0.1l24.1-1.9l4.6-0.2l0,6.4l0.2,16.7l-0.8,31l-0.2,14.1l2.7,18.8L624.6,467z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"MSn\" x=\"587\" y=\"428\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="MT"):
   statemapoutput = statemapoutput + "   <path id=\"MT\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M356.7,122.3l0.6-11.2l2.3-24.8c0.5-5,1.1-8.5,1.4-15.4l0.9-14.6l-30.7-2.8L302,50l-29.3-4 l-32.3-5.3l-18.4-3.4l-32.7-6.9l-4.5,21.3l3.4,7.5l-1.4,4.6l1.8,4.6l3.2,1.4l4.6,10.8l2.7,3.2l0.5,1.1l3.4,1.1l0.5,2.1l-7.1,17.6 v2.5l2.5,3.2h0.9l4.8-3l0.7-1.1l1.6,0.7l-0.2,5.3l2.7,12.6l3,2.5l0.9,0.7l1.8,2.3l-0.5,3.4l0.7,3.4l1.1,0.9l2.3-2.3h2.7l3.2,1.6 l2.5-0.9h4.1l3.7,1.6l2.7-0.5l0.5-3l3-0.7l1.4,1.4l0.5,3.2l1.8,1.4l1.5-11.6l20.7,3l28.2,4l16.6,1.9l31.4,3.5l11,1.5l1.1-15.4 L356.7,122.3z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"MTn\" x=\"270\" y=\"100\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="NC"):
   statemapoutput = statemapoutput + "   <path id=\"NC\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M832.1,298.5l1.7,4.7l3.6,6.5l2.4,2.4l0.6,2.3l-2.4,0.2l0.8,0.6l-0.3,4.2l-2.6,1.3l-0.6,2.1 l-1.3,2.9l-3.7,1.6l-2.4-0.3l-1.5-0.2l-1.6-1.3l0.3,1.3v1h1.9l0.8,1.3l-1.9,6.3h4.2l0.6,1.6l2.3-2.3l1.3-0.5l-1.9,3.6l-3.1,4.8 h-1.3l-1.1-0.5l-2.7,0.6l-5.2,2.4l-6.5,5.3l-3.4,4.7l-1.9,6.5l-0.5,2.4l-4.7,0.5l-5.5,1.3l-9.9-8.2l-12.6-7.6l-2.9-0.8l-12.6,1.5 l-4.3,0.8l-1.6-3.2l-3-2.1l-16.5,0.5l-7.3,0.8l-9.1,4.5l-6.1,2.6l-1.6,0.3l-5.8,1l-7,0.8l-6.8,0.5l0.5-4.1l1.8-1.5l2.7-0.6l0.6-3.7 l4.2-2.7l3.9-1.5l4.2-3.6l4.4-2.1l0.6-3.1l3.9-3.9l0.6-0.2c0,0,0,1.1,0.8,1.1c0.8,0,1.9,0.3,1.9,0.3l2.3-3.6l2.1-0.6l2.3,0.3 l1.6-3.6l2.9-2.6l0.5-2.1v-4l4.5,0.7l7.1-1.3l15.8-1.9l17.1-2.6l19.9-4l19.7-4.2l11.4-2.8L832.1,298.5z M836,331.5l2.6-2.5 l3.2-2.6l1.5-0.6l0.2-2l-0.6-6.1l-1.5-2.3l-0.6-1.9l0.7-0.2l2.7,5.5l0.4,4.4l-0.2,3.4l-3.4,1.5l-2.8,2.4l-1.1,1.2L836,331.5z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"NCn\" x=\"763\" y=\"342\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="ND"):
   statemapoutput = statemapoutput + "   <path id=\"ND\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M471.3,127.7l-0.4-7.5l-2-7.3l-1.8-13.6l-0.5-9.8l-2-3.1l-1.6-5.4v-10.3l0.7-3.9l-2.1-5.5 l-28.4-0.6l-18.6-0.6l-26.5-1.3l-24.9-1.9l-1.3,14.2l-1.4,15.1l-2.3,24.9l-0.5,11l56.8,3.8L471.3,127.7z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"NDn\" x=\"405\" y=\"103\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="NE"):
   if(winning_candidate_states_split[il]!=winning_candidate_states_split[il+1] and winning_candidate_states_split[il]!=winning_candidate_states_split[il+2]):
    statemapoutput = statemapoutput + "   <path id=\"NE\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M484.2,247l1.4,2.7l0.1,2.1l2.4,3.7l2.7,3.2h-5l-43.5-0.9l-40.8-0.9l-21.2-1l1.1-21.3l-33.4-2.7 l4.3-44l15.5,1L388,190l17.8,1.1l23.8,1.1l10.7-0.5l2.1,2.3l4.8,3l1.1,0.9l4.3-1.4l3.9-0.5l2.7-0.2l1.8,1.4l5,1.6l3,1.6l0.5,1.6 l0.9,2.1h1.8l0.8,0l1,5.2l2.7,8l1.2,4.6l2.1,3.8l0.5,4.9l1.4,4.3l0.5,6.5\"/>\n"
    statetextoutput = statetextoutput + "   <text id=\"NEn\" x=\"411\" y=\"232\">"+str(electoral_college_points_split[il])+"</text>\n";
    candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
   if(winning_candidate_states_split[il]==winning_candidate_states_split[il+1] and winning_candidate_states_split[il]!=winning_candidate_states_split[il+2]):
    statemapoutput = statemapoutput + "   <path id=\"NE\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M484.2,247l1.4,2.7l0.1,2.1l2.4,3.7l2.7,3.2h-5l-43.5-0.9l-40.8-0.9l-21.2-1l1.1-21.3l-33.4-2.7 l4.3-44l15.5,1L388,190l17.8,1.1l23.8,1.1l10.7-0.5l2.1,2.3l4.8,3l1.1,0.9l4.3-1.4l3.9-0.5l2.7-0.2l1.8,1.4l5,1.6l3,1.6l0.5,1.6 l0.9,2.1h1.8l0.8,0l1,5.2l2.7,8l1.2,4.6l2.1,3.8l0.5,4.9l1.4,4.3l0.5,6.5\"/>\n"
    statetextoutput = statetextoutput + "   <text id=\"NEn\" x=\"411\" y=\"232\">"+str(electoral_college_points_split[il] + 1)+"</text>\n";
    candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il] + 1;
   if(winning_candidate_states_split[il]!=winning_candidate_states_split[il+1] and winning_candidate_states_split[il]==winning_candidate_states_split[il+2]):
    statemapoutput = statemapoutput + "   <path id=\"NE\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M484.2,247l1.4,2.7l0.1,2.1l2.4,3.7l2.7,3.2h-5l-43.5-0.9l-40.8-0.9l-21.2-1l1.1-21.3l-33.4-2.7 l4.3-44l15.5,1L388,190l17.8,1.1l23.8,1.1l10.7-0.5l2.1,2.3l4.8,3l1.1,0.9l4.3-1.4l3.9-0.5l2.7-0.2l1.8,1.4l5,1.6l3,1.6l0.5,1.6 l0.9,2.1h1.8l0.8,0l1,5.2l2.7,8l1.2,4.6l2.1,3.8l0.5,4.9l1.4,4.3l0.5,6.5\"/>\n"
    statetextoutput = statetextoutput + "   <text id=\"NEn\" x=\"411\" y=\"232\">"+str(electoral_college_points_split[il] + 1)+"</text>\n";
    candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il] + 1;
   if(winning_candidate_states_split[il]==winning_candidate_states_split[il+1] and winning_candidate_states_split[il]==winning_candidate_states_split[il+2]):
    statemapoutput = statemapoutput + "   <path id=\"NE\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M484.2,247l1.4,2.7l0.1,2.1l2.4,3.7l2.7,3.2h-5l-43.5-0.9l-40.8-0.9l-21.2-1l1.1-21.3l-33.4-2.7 l4.3-44l15.5,1L388,190l17.8,1.1l23.8,1.1l10.7-0.5l2.1,2.3l4.8,3l1.1,0.9l4.3-1.4l3.9-0.5l2.7-0.2l1.8,1.4l5,1.6l3,1.6l0.5,1.6 l0.9,2.1h1.8l0.8,0l1,5.2l2.7,8l1.2,4.6l2.1,3.8l0.5,4.9l1.4,4.3l0.5,6.5\"/>\n"
    statetextoutput = statetextoutput + "   <text id=\"NEn\" x=\"411\" y=\"232\">"+str(electoral_college_points_split[il] + 2)+"</text>\n";
    candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il] + 2;
  if(state_initials_split[il]=="NE-1"):
   if(winning_candidate_states_split[il]!=winning_candidate_states_split[il-1] and winning_candidate_states_split[il]!=winning_candidate_states_split[il+1]):
    statemapoutput = statemapoutput + "<circle id=\"NE-1\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" cx=\"459\" cy=\"239\" r=\"14\"/>\n"
    statetextoutput = statetextoutput + "   <text id=\"NE-1n\" x=\"451\" y=\"248\" font-size=\"25\">"+str(electoral_college_points_split[il])+"</text>\n";
    candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
   if(winning_candidate_states_split[il]!=winning_candidate_states_split[il-1] and winning_candidate_states_split[il]==winning_candidate_states_split[il+1]):
    statemapoutput = statemapoutput + "<circle id=\"NE-1\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" cx=\"459\" cy=\"239\" r=\"14\"/>\n"
    statetextoutput = statetextoutput + "   <text id=\"NE-1n\" x=\"451\" y=\"248\" font-size=\"25\">"+str(electoral_college_points_split[il] + 1)+"</text>\n";
    candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il] + 1;
  if(state_initials_split[il]=="NE-2"):
   if(winning_candidate_states_split[il]!=winning_candidate_states_split[il-2] and winning_candidate_states_split[il]!=winning_candidate_states_split[il-1]):
    statemapoutput = statemapoutput + "<circle id=\"NE-1\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" cx=\"459\" cy=\"239\" r=\"14\"/>\n"
    statetextoutput = statetextoutput + "   <text id=\"NE-1n\" x=\"371\" y=\"216\" font-size=\"25\">"+str(electoral_college_points_split[il])+"</text>\n";
    candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="NH"):
   statemapoutput = statemapoutput + "   <path id=\"NH\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M880.8,142.4l0.9-1.1l1.1-3.3l-2.5-0.9l-0.5-3.1l-3.9-1.1l-0.3-2.7l-7.3-23.4l-4.6-14.5l-0.9,0 l-0.6,1.6l-0.6-0.5l-1-1l-1.5,1.9l0,5l0.3,5.7l1.9,2.7v4l-3.7,5.1l-2.6,1.1v1.1l1.1,1.8v8.6l-0.8,9.2l-0.2,4.8l1,1.3l-0.2,4.5 l-0.5,1.8l1.5,0.9l16.4-4.7l2.3-0.6l1.5-2.6L880.8,142.4z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"NHn\" x=\"800\" y=\"58\" font-size=\"22\">NH "+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="NJ"):
   statemapoutput = statemapoutput + "   <path id=\"NJ\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M828.2,190.3l-2.1,2.4v3.1l-1.9,3.1l-0.2,1.6l1.3,1.3l-0.2,2.4l-2.3,1.1l0.8,2.7l0.2,1.1l2.7,0.3 l1,2.6l3.6,2.4l2.4,1.6v0.8l-3.2,3.1l-1.6,2.3l-1.5,2.7l-2.3,1.3l-1.2,0.7l-0.2,1.2l-0.6,2.6l1.1,2.2l3.2,2.9l4.8,2.3l4,0.6 l0.2,1.5l-0.8,1l0.3,2.7h0.8l2.1-2.4l0.8-4.8l2.7-4l3.1-6.5l1.1-5.5l-0.6-1.1l-0.2-9.4l-1.6-3.4l-1.1,0.8l-2.7,0.3l-0.5-0.5l1.1-1 l2.1-1.9l0.1-1.1l-0.4-3.4l0.5-2.7l-0.2-2.1l-2.6-1.1l-4.5-1l-3.9-1.1L828.2,190.3z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"NJn\" x=\"898\" y=\"260\" font-size=\"22\">NJ "+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="NM"):
   statemapoutput = statemapoutput + "   <path id=\"NM\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M282.7,431l-0.7-6.1l8.6,0.5l29.5,3.1l28.4,1.4l2-22.3l3.7-55.9l1.1-19.4l2,0.3l0-11.1l-32.2-2.4 l-36.9-4.4l-34.5-4.1l-4.2,30.8l-7,53.2l-3.8,26.9l-2,13.3l15.5,2l1.3-10l16.7,2.6L282.7,431z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"NMn\" x=\"290\" y=\"381\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="NV"):
   statemapoutput = statemapoutput + "   <path id=\"NV\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M140.7,177.6l21,4.5l9.7,1.9l9.3,1.8l6.6,1.6l-0.6,5.9l-3.5,17.3l-4.1,20l-1.9,9.7l-2.2,13.3 l-3.2,16.4l-3.5,15.7l-2,10.2l-2.5,16.8l-0.5,1.1l-1.1,2.5l-1.9-0.1l-1.1-2.7l-2.7-0.5l-1.4-1l-2,0.3l-0.9,0.7l-1.3,1.3l-0.4,7 l-0.5,1.7l-0.4,12.1l-1.3,1.7l-1.9-2.3l-14.5-22.7l-19.4-29L89.6,249l-12.4-18.6l1.6-6.6l7-25.9l7.9-31.3l33.6,8.1l13.7,3\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"NVn\" x=\"120\" y=\"242\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="NY"):
   statemapoutput = statemapoutput + "   <path id=\"NY\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M828.9,189.3l-1.1-1l-2.6-0.2l-2.3-1.9l-1.6-6.1l-3.5,0.1l-2.4-2.7l-19.4,4.4l-43,8.7l-7.5,1.2 l-0.7-6.5l1.4-1.1l1.3-1.1l1-1.6l1.8-1.1l1.9-1.8l0.5-1.6l2.1-2.7l1.1-1l-0.2-1l-1.3-3.1l-1.8-0.2l-1.9-6.1l2.9-1.8l4.4-1.5l4-1.3 l3.2-0.5l6.3-0.2l1.9,1.3l1.6,0.2l2.1-1.3l2.6-1.1l5.2-0.5l2.1-1.8l1.8-3.2l1.6-1.9h2.1l1.9-1.1l0.2-2.3l-1.5-2.1l-0.3-1.5l1.1-2.1 v-1.5h-1.8l-1.8-0.8l-0.8-1.1l-0.2-2.6l5.8-5.5l0.6-0.8l1.5-2.9l2.9-4.5l2.7-3.7l2.1-2.4l2.4-1.8l3.1-1.2l5.5-1.3l3.2,0.2l4.5-1.5 l7.6-2.1l0.5,5l2.4,6.5l0.8,5.2l-1,3.9l2.6,4.5l0.8,2.1l-0.8,2.9l2.9,1.3l0.6,0.3l3.1,11l-0.5,5.1l-0.5,10.8l0.8,5.5l0.8,3.6 l1.5,7.3v8.1l-1.1,2.3l1.8,2l0.8,1.7l-1.9,1.8l0.3,1.3l1.3-0.3l1.5-1.3l2.3-2.6l1.1-0.6l1.6,0.6l2.3,0.2l7.9-3.9l2.9-2.7l1.3-1.5 l4.2,1.6l-3.4,3.6l-3.9,2.9l-7.1,5.3l-2.6,1l-5.8,1.9l-4,1.1l-1.2-0.5l-0.2-3.7l0.5-2.7l-0.2-2.1l-2.8-1.7l-4.5-1l-3.9-1.1 L828.9,189.3z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"NYn\" x=\"798\" y=\"167\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="OH"):
   statemapoutput = statemapoutput + "   <path id=\"OH\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M731.4,195l-6.1,4.1l-3.9,2.3l-3.4,3.7l-4,3.9l-3.2,0.8l-2.9,0.5l-5.5,2.6l-2.1,0.2l-3.4-3.1 l-5.2,0.6l-2.6-1.5l-2.4-1.4l-4.9,0.7l-10.2,1.6l-7.8,1.2l1.3,14.6l1.8,13.7l2.6,23.4l0.6,4.8l4.1-0.1l2.4-0.8l3.4,1.5l2.1,4.4 l5.1,0l1.9,2.1l1.8-0.1l2.5-1.3l2.5,0.4l2,1.5l1.7-2.1l2.3-1.3l2.1-0.7l0.6,2.7l1.8,1l3.5,2.3l2.2-0.1l1.1-1.1l-0.1-1.4l1.6-1.5 l0.2-5l1-3.9l1.5-1.4l1.5,0.9l0.8,1.2l1.2-0.2l-0.4-2.4l-0.6-0.6v-2.4l1-1.3l2.3-3.4l1.3-1.5l2.1,0.5l2.3-1.6l3.1-3.4l2.3-3.9 l0.2-5.4l0.5-5v-4.7l-1.1-3.1l1-1.5l0.9-1l-1.4-9.8L731.4,195z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"OHn\" x=\"685\" y=\"248\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="OK"):
   statemapoutput = statemapoutput + "   <path id=\"OK\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M375.3,322.6l-10.7-0.5l-6.4-0.5l0.3,0.2l-0.7,10.4l22,1.4l32.1,1.3l-2.3,24.4l-0.5,17.8l0.2,1.6 l4.3,3.7l2.1,1.1l0.7-0.2l0.7-2.1l1.4,1.8h2.1v-1.4l2.7,1.4l-0.5,3.9l4.1,0.2l2.5,1.1l4.1,0.7l2.5,1.8l2.3-2.1l3.4,0.7l2.5,3.4h0.9 v2.3l2.3,0.7l2.3-2.3l1.8,0.7h2.5l0.9,2.5l4.8,1.8l1.4-0.7l1.8-4.1h1.1l1.1,2.1l4.1,0.7l3.7,1.4l3,0.9l1.8-0.9l0.7-2.5h4.3l2.1,0.9 l2.7-2.1h1.1l0.7,1.6h4.1l1.6-2.1l1.8,0.5l2.1,2.5l3.2,1.8l3.2,0.9l1.9,1.1l-0.4-37.2l-1.4-11l-0.2-8.9l-1.4-6.5l-0.8-7.2l-0.1-3.8 l-12.1,0.3l-46.4-0.5l-45-2.1L375.3,322.6z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"OKn\" x=\"451\" y=\"370\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="OR"):
   statemapoutput = statemapoutput + "   <path id=\"OR\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M140.2,176.8l4.3-17.9l4.7-17.9l1.1-4.2l2.4-5.6l-0.6-1.2l-2.5,0l-1.3-1.7l0.5-1.5l0.5-3.2l4.5-5.5 l1.8-1.1l1.1-1.1l1.5-3.6l4-5.7l3.6-3.9l0.2-3.5l-3.3-2.5l-1.2-4.5l-13.2-3.7l-15.1-3.5l-15.4,0.1l-0.5-1.4l-5.5,2.1l-4.5-0.6 l-2.4-1.6l-1.3,0.7L99,84l-1.7-1.3l-5.3-2h-0.8l-4.3-1.4l-1.9,1.8l-6.2-0.3l-5.9-4.1l0.7-0.8l0.2-7.8l-2.3-3.9l-4.1-0.6 l-0.7-2.5l-2.4-0.5l-5.8,2.1l-2.3,6.5l-3.2,10l-3.2,6.5l-5,14.1l-6.5,13.6l-8.1,12.6l-1.9,2.9l-0.8,8.6l-1.3,6l2.7,3.5l6.7,2.3 l11.6,3.3l7.9,2.5l12.4,3.6l13.3,3.6l13.2,3.6\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"ORn\" x=\"88\" y=\"136\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="PA"):
   statemapoutput = statemapoutput + "   <path id=\"PA\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M822.2,226.3l1.1-0.6l2.3-0.6l1.5-2.7l1.6-2.3l3.2-3.1v-0.8l-2.4-1.6l-3.6-2.4l-1-2.6l-2.7-0.3 l-0.2-1.1l-0.8-2.7l2.3-1.1l0.2-2.4l-1.3-1.3l0.2-1.6l1.9-3.1v-3.1l2.3-2.4l0.2-1.1l-2.6-0.2l-2.3-1.9l-2.4-5.3l-3-0.9l-2.3-2.1 l-18.6,4l-43,8.7l-8.9,1.5l-0.5-7.1l-5.5,5.6l-1.3,0.5l-4.2,3l2.9,19.1l2.9,9.5l3.6,19.3l3.3-0.6l11.9-1.5l37.9-7.7l14.9-2.8 l8.3-1.6l0.3-0.2l2.1-1.6L822.2,226.3z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"PAn\" x=\"764\" y=\"220\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="RI"):
   statemapoutput = statemapoutput + "   <path id=\"RI\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M874.1,179.8l-0.5-4.2l-0.8-4.4l-1.7-5.9l5.7-1.5l1.6,1.1l3.4,4.4l2.9,4.4l-2.9,1.5l-1.3-0.2 l-1.1,1.8l-2.4,1.9L874.1,179.8z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"RIn\" x=\"925\" y=\"199\" font-size=\"22\">RI "+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="SC"):
   statemapoutput = statemapoutput + "   <path id=\"SC\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M761.2,412.9l-1.8,1l-2.6-1.3l-0.6-2.1l-1.3-3.6l-2.3-2.1l-2.6-0.6l-1.6-4.8l-2.7-6l-4.2-1.9 l-2.1-1.9l-1.3-2.6L736,385l-2.3-1.3l-2.3-2.9l-3.1-2.3l-4.5-1.8l-0.5-1.5l-2.4-2.9l-0.5-1.5l-3.4-5.2l-3.4,0.2l-4-2.4l-1.3-1.3 l-0.3-1.8l0.8-1.9l2.3-1l-0.3-2.1l6.1-2.6l9.1-4.5l7.3-0.8l16.5-0.5l2.3,1.9l1.6,3.2l4.4-0.5l12.6-1.5l2.9,0.8l12.6,7.6l10.1,8.1 l-5.4,5.5l-2.6,6.1l-0.5,6.3l-1.6,0.8l-1.1,2.7l-2.4,0.6l-2.1,3.6l-2.7,2.7l-2.3,3.4l-1.6,0.8l-3.6,3.4l-2.9,0.2l1,3.2l-5,5.5 L761.2,412.9z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"SCn\" x=\"745\" y=\"380\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="SD"):
   statemapoutput = statemapoutput + "   <path id=\"SD\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M472.8,203.2l-1-1.1l-1.5-3.6l1.8-3.7l1.1-5.6l-2.6-2.1l-0.3-2.7l0.6-3l2.2-0.8l0.3-5.7l-0.1-30.1 l-0.6-3l-4.1-3.6l-1-2v-1.9l1.9-1.3l1.5-1.9l0.2-2.7l-57.4-1.6l-56.2-3.9l-0.8,5.3l-1.6,15.9l-1.3,17.9l-1.6,24.6l16,1l19.6,1.1 l18,1.3l23.8,1.3l10.7-0.8l2.9,2.3l4.3,3l1,0.8l3.5-0.9l4-0.3l2.7-0.1l3.1,1.2l4.5,1.4l3.1,1.8l0.6,1.9l0.9,1.9l0.7-0.5 L472.8,203.2z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"SDn\" x=\"405\" y=\"170\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="TN"):
   statemapoutput = statemapoutput + "   <path id=\"TN\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M697.1,320.6l-51.9,5l-15.8,1.8l-4.6,0.5l-3.9,0v3.9l-8.4,0.5l-7,0.6l-11.1,0.1l-0.3,5.8l-2.1,6.3 l-1,3l-1.3,4.4l-0.3,2.6l-4,2.3l1.5,3.6l-1,4.4l-1,0.8l7.3-0.2l24.1-1.9l5.3-0.2l8.1-0.5l27.8-2.6l10.2-0.8l8.4-1l8.4-1.1l4.8-0.8 l-0.1-4.5l1.8-1.5l2.7-0.6l0.6-3.7l4.2-2.7l3.9-1.5l4.2-3.6l4.4-2.1l0.9-3.5l4.3-3.9l0.6-0.2c0,0,0,1.1,0.8,1.1s1.9,0.3,1.9,0.3 l2.3-3.6l2.1-0.6l2.3,0.3l1.6-3.6l2.1-2.2l0.6-1l0.2-3.9l-1.5-0.3l-2.4,1.9l-7.9,0.2l-12,1.9L697.1,320.6z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"TNn\" x=\"633\" y=\"353\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="TX"):
   statemapoutput = statemapoutput + "   <path id=\"TX\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M357.1,333.4l22.7,1.1l31.1,1.1l-2.3,23.5l-0.3,18.2l0.1,2.1l4.3,3.8l1.7,0.8l1.8,0.3l0.7-1.3 l0.9,0.9l1.7,0.5l1.6-0.7l1.1,0.4l-0.3,3.4l4.3,1l2.7,0.8l4,0.5l2.2,1.8l3.2-1.6l2.8,0.4l2,2.8l1.1,0.3l-0.2,2l3.1,1.2l2.8-1.8 l1.5,0.4l2.4,0.2l0.4,1.9l4.6,2l2.7-0.2l2-4.1h0.3l1.1,1.9l4.4,1l3.3,1.2l3.3,0.8l2.1-0.8l0.8-2.5h3.7l1.9,0.8l3.1-1.6h0.7l0.4,1.1 h4.3l2.4-1.3l1.7,0.3l1.4,1.9l2.9,1.7l3.5,1.1l2.7,1.4l2.4,1.6l3.3-0.9l1.9,1l0.5,10.1l0.3,9.7l0.7,9.5l0.5,4l2.7,4.6l1.1,4.1 l3.9,6.3l0.5,2.9l0.5,1l-0.7,7.5l-2.7,4.4l1,2.9l-0.4,2.5l-0.8,7.3l-1.4,2.7l0.6,4.4l-5.7,1.6l-9.9,4.5l-1,1.9l-2.6,1.9l-2.1,1.5 l-1.3,0.8l-5.7,5.3l-2.7,2.1l-5.3,3.2l-5.7,2.4l-6.3,3.4l-1.8,1.5l-5.8,3.6l-3.4,0.6l-3.9,5.5l-4,0.3l-1,1.9l2.3,1.9l-1.5,5.5 l-1.3,4.5l-1.1,3.9l-0.8,4.5l0.8,2.4l1.8,7l1,6.1l1.8,2.7l-1,1.5l-3.1,1.9l-5.7-3.9l-5.5-1.1l-1.3,0.5l-3.2-0.6l-4.2-3.1l-5.2-1.1 l-7.6-3.4l-2.1-3.9l-1.3-6.5l-3.2-1.9l-0.6-2.3l0.6-0.6l0.3-3.4l-1.3-0.6l-0.6-1l1.3-4.4l-1.6-2.3l-3.2-1.3l-3.4-4.4l-3.6-6.6 l-4.2-2.6l0.2-1.9l-5.3-12.3l-0.8-4.2l-1.8-1.9l-0.2-1.5l-6-5.3l-2.6-3.1v-1.1l-2.6-2.1l-6.8-1.1l-7.4-0.6l-3.1-2.3l-4.5,1.8 l-3.6,1.5l-2.3,3.2l-1,3.7l-4.4,6.1l-2.4,2.4l-2.6-1l-1.8-1.1l-1.9-0.6l-3.9-2.3v-0.6l-1.8-1.9l-5.2-2.1l-7.4-7.8l-2.3-4.7v-8.1 l-3.2-6.5l-0.5-2.7l-1.6-1l-1.1-2.1l-5-2.1l-1.3-1.6l-7.1-7.9l-1.3-3.2l-4.7-2.3l-1.5-4.4l-2.6-2.9l-1.9-0.5l-0.6-4.7l8,0.7l29,2.7 l29.3,1.6l2.3-23.8l3.9-55.6l1.6-18.7l1.4,0 M457.2,567.3l-0.6-7.1l-2.7-7.2l-0.6-7l1.5-8.2l3.3-6.9l3.5-5.4l3.2-3.6l0.6,0.2 l-4.8,6.6l-4.4,6.5l-2,6.6l-0.3,5.2l0.9,6.1l2.6,7.2l0.5,5.2l0.2,1.5L457.2,567.3z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"TXn\" x=\"410\" y=\"458\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="UT"):
   statemapoutput = statemapoutput + "   <path id=\"UT\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M253,309.3l-24.6-3.5l-26.6-4.9l-33.8-6l1.6-9.2l3.2-15.2L176,254l2.2-13.6l1.9-8.9l3.8-20.5 l3.5-17.5l1.1-5.6l12.7,2.3l12,2.1l10.3,1.8l8.3,1.4l3.7,0.5l-1.5,10.6l-2.3,13.2l7.8,0.9l16.4,1.8l8.2,0.9l-2.1,22l-3.2,22.6 l-3.8,27.8l-1.7,11.1L253,309.3z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"UTn\" x=\"209\" y=\"265\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="VA"):
   statemapoutput = statemapoutput + "   <path id=\"VA\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M828.9,269.2l-0.1-1.9l6.5-2.5l-0.8,3.2l-2.9,3.8l-0.4,4.6l0.5,3.4l-1.8,5l-2.2,1.9l-1.5-4.6 l0.4-5.4l1.6-4.2L828.9,269.2z M831.2,297.5L773,310.1l-37.4,5.3l-6.7-0.4l-2.6,1.9l-7.3,0.2l-8.4,1l-8.9,1l8.5-4.9l0-2.1 l1.5-2.1l10.6-11.5l3.9,4.5l3.8,1l2.5-1.1l2.2-1.3l2.5,1.3l3.9-1.4l1.9-4.6l2.6,0.5l2.9-2.1l1.8,0.5l2.8-3.7l0.3-2.1l-1-1.3l1-1.9 l5.3-12.3l0.6-5.7l1.2-0.5l2.2,2.4l3.9-0.3l1.9-7.6l2.8-0.6l1-2.7l2.6-2.3l1.3-2.3l1.5-3.4l0.1-5.1l9.8,3.8 c0.7,0.3,0.7-4.8,0.7-4.8l4.1,1.4l-0.5,2.6l8.2,2.9l1.3,1.8l-0.9,3.7l-1.3,1.3l-0.5,1.7l0.5,2.4l2,1.3l3.9,1.4l2.9,1l4.9,0.9 l2.2,2.1l3.2,0.4l0.9,1.2l-0.4,4.7l1.4,1.1l-0.5,1.9l1.2,0.8l-0.2,1.4l-2.7-0.1l0.1,1.6l2.3,1.5l0.1,1.4l1.8,1.8l0.5,2.5l-2.6,1.4 l1.6,1.5l5.8-1.7L831.2,297.5z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"VAn\" x=\"767\" y=\"294\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="VT"):
   statemapoutput = statemapoutput + "   <path id=\"VT\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M844.3,153.7l-0.8-5.7l-2.4-10l-0.6-0.3l-2.9-1.3l0.8-2.9l-0.8-2.1l-2.7-4.6l1-3.9l-0.8-5.2 l-2.4-6.5l-0.8-4.9l26.2-6.7l0.3,5.8l1.9,2.7v4l-3.7,4l-2.6,1.1v1.1l1.1,1.8v8.6l-0.8,9.2l-0.2,4.8l1,1.3l-0.2,4.5l-0.5,1.8 l0.7,1.6l-7,1.4L844.3,153.7z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"VTn\" x=\"790\" y=\"82\" font-size=\"22\">VT "+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="WA"):
   statemapoutput = statemapoutput + "   <path id=\"WA\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M93.6,6.4l4.4,1.5l9.7,2.7l8.6,1.9l20,5.7l23,5.7l15.2,3.4l-1,3.9l-4.1,13.8l-4.5,20.8 l-3.2,16.1l-0.4,9.4l-13.2-3.9l-15.6-3.4l-13.7,0.6l-1.6-1.5l-5.3,1.9l-4-0.3l-2.7-1.8l-1.6,0.5l-4.2-0.2l-1.9-1.4l-4.8-1.7 l-1.4-0.2l-5-1.3l-1.8,1.5l-5.7-0.3l-4.8-3.8l0.2-0.8l0.1-7.9l-2.1-3.9l-4.1-0.7l-0.4-2.4l-2.5-0.6l-2.9-0.5l-1.8,1l-2.3-2.9 l0.3-2.9l2.7-0.3l1.6-4l-2.6-1.1l0.2-3.7l4.4-0.6l-2.7-2.7l-1.5-7.1l0.6-2.9v-7.9l-1.8-3.2l2.3-9.4l2.1,0.5l2.4,2.9l2.7,2.6 l3.2,1.9l4.5,2.1l3.1,0.6l2.9,1.5l3.4,1l2.3-0.2v-2.4l1.3-1.1l2.1-1.3l0.3,1.1l0.3,1.8l-2.3,0.5l-0.3,2.1l1.8,1.5l1.1,2.4l0.6,1.9 l1.5-0.2l0.2-1.3l-1-1.3l-0.5-3.2l0.8-1.8l-0.6-1.5V19l1.8-3.6l-1.1-2.6l-2.4-4.8l0.3-0.8L93.6,6.4z M84.1,12.3l2-0.2 l0.5,1.4l1.5-1.6h2.3l0.8,1.5l-1.5,1.7l0.6,0.8l-0.7,2l-1.4,0.4c0,0-0.9,0.1-0.9-0.2s1.5-2.6,1.5-2.6l-1.7-0.6l-0.3,1.5l-0.7,0.6 l-1.5-2.3L84.1,12.3z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"WAn\" x=\"105\" y=\"62\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="WI"):
   statemapoutput = statemapoutput + "   <path id=\"WI\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M612.9,197.2l0.4-3l-1.6-4.5l-0.6-6.1l-1.1-2.4l1-3.1l0.8-2.9l1.5-2.6l-0.6-3.4l-0.6-3.6l0.5-1.8 l1.9-2.4l0.2-2.7l-0.8-1.3l0.6-2.6l0.5-3.2l2.7-5.7l2.9-6.8l0.2-2.3l-0.3-1l-0.8,0.5l-4.2,6.3l-2.7,4l-1.9,1.8l-0.8,2.3l-1.5,0.8 l-1.1,1.9l-1.5-0.3l-0.2-1.8l1.3-2.4l2.1-4.7l1.8-1.6l1.1-2.3l-1.6-0.9l-1.4-1.4l-1.6-10.3l-3.7-1.1l-1.4-2.3l-12.6-2.7l-2.5-1.1 l-8.2-2.3l-8.2-1.1l-4.2-5.4l-0.5,1.3l-1.1-0.2l-0.6-1.1l-2.7-0.8l-1.1,0.2l-1.8,1l-1-0.6l0.6-1.9l1.9-3.1l1.1-1.1l-1.9-1.5 l-2.1,0.8l-2.9,1.9l-7.4,3.2l-2.9,0.6l-2.9-0.5l-1-0.9l-2.1,2.8l-0.2,2.7v8.5l-1.1,1.6l-5.3,3.9l-2.3,5.9l0.5,0.2l2.5,2.1l0.7,3.2 l-1.8,3.2v3.9l0.5,6.6l3,3h3.4l1.8,3.2l3.4,0.5l3.9,5.7l7.1,4.1l2.1,2.7l0.9,7.4l0.7,3.3l2.3,1.6l0.2,1.4l-2.1,3.4l0.2,3.2l2.5,3.9 l2.5,1.1l3,0.5l1.3,1.4l9.2,0l26.1-1.5L612.9,197.2z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"WIn\" x=\"561\" y=\"163\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="WV"):
   statemapoutput = statemapoutput + "   <path id=\"WV\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M756.4,242.2l1.1,4.9l1.1,6.9l3.6-2.7l2.3-3.1l2.5-0.6l1.5-1.5l1.8-2.6l1.2,0.6l2.9-0.3l2.6-2.1 l2-1.5l1.8-0.5l1.3,1l2.2,1.1l1.9,1.8l1.4,1.3l-0.1,4.7l-5.7-3.1l-4.5-1.8l-0.2,5.3l-0.5,2.1l-1.6,2.7l-0.6,1.6l-3.1,2.4l-0.5,2.3 l-3.4,0.3l-0.3,3.1l-1.1,5.5h-2.6l-1.3-0.8l-1.6-2.7l-1.8,0.2l-0.3,4.4l-2.1,6.6l-5,10.8l0.8,1.3l-0.2,2.7l-2.1,1.9l-1.5-0.3 l-3.2,2.4l-2.6-1l-1.8,4.7c0,0-3.7,0.8-4.4,1c-0.6,0.2-2.4-1.3-2.4-1.3l-2.4,2.3l-2.6,0.6l-2.9-0.8l-1.3-1.3l-2.2-3l-3.1-2 l-2.6-2.7l-2.9-3.7l-0.6-2.3l-2.6-1.5l-0.8-1.6l-0.2-5.3l2.2-0.1l1.9-0.8l0.2-2.7l1.6-1.5l0.2-5l1-3.9l1.3-0.6l1.3,1.1l0.5,1.8 l1.8-1l0.5-1.6l-1.1-1.8v-2.4l1-1.3l2.3-3.4l1.3-1.5l2.1,0.5l2.3-1.6l3.1-3.4l2.3-3.9l0.3-5.7l0.5-5v-4.7l-1.1-3.1l1-1.5l1.3-1.3 l3.5,19.8l4.6-0.8L756.4,242.2z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"WVn\" x=\"730\" y=\"281\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  if(state_initials_split[il]=="WY"):
   statemapoutput = statemapoutput + "   <path id=\"WY\" fill=\""+candidate_colors_split[winning_candidate_states_split[il]]+"\" d=\"M354.3,143.8l-10.5-0.8l-32.1-3.3l-16.2-2.1l-28.3-4.1l-19.9-3l-1.4,11.2l-3.8,24.3l-5.3,30.4 l-1.5,10.5l-1.7,11.9l6.5,0.9l25.9,2.5l20.6,2.3l36.8,4.1l23.8,2.9l4.5-44.2l1.4-25.4L354.3,143.8z\"/>\n"
   statetextoutput = statetextoutput + "   <text id=\"WYn\" x=\"290\" y=\"191\">"+str(electoral_college_points_split[il])+"</text>\n";
   candidate_electoral_points_split[winning_candidate_states_split[il]] = candidate_electoral_points_split[winning_candidate_states_split[il]] + electoral_college_points_split[il];
  il = il + 1;
 statemapoutput = statemapoutput + statemapoutput_dclast + "  </g>\n";
 statetextoutput = statetextoutput + statetextoutput_dclast;
 if(len(candidate_short_names_split)==2):
  svg_file_width = 1020;
  long_candidate_short_name = candidate_short_names_split[0]+" "+str(candidate_electoral_points_split[0]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]))):
   long_candidate_short_name = candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]);
  svg_file_width = svg_file_width + ( len(long_candidate_short_name) * 10 );
  outputsvgstring = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>
 <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"%s\" height=\"593\">
  <title>%s US presidential election results</title>
""" % (str(svg_file_width), electoral_year);
  statetextoutput = statetextoutput + """ <text id=\"DemL\" x=\"855\" y=\"392\">%s</text>
 <text id=\"RepL\" x=\"855\" y=\"425\">%s</text>
  </g>
 <path id=\"lines\" d=\"M844,62l13,29M832,86l8,17M889,153l34,3M882,178l41,12M866,184l51 33M845,230l50,22M837,250l51,26M833,261l46,33M800,251l61,61\" stroke=\"#000000\" stroke-width=\"1.6\"/>
 <rect id=\"Dem\" x=\"828\" y=\"373\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Rep\" x=\"828\" y=\"406\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <path id=\"frames\" fill=\"none\" stroke=\"#A9A9A9\" stroke-width=\"2\" d=\"M215,493v55l36,45 M0,425h147l68,68h85l54,54v46\"/>
</svg>""" % (candidate_short_names_split[0]+" "+str(candidate_electoral_points_split[0]), candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]), candidate_colors_split[0], candidate_colors_split[1]);
 if(len(candidate_short_names_split)==3):
  svg_file_width = 1020;
  long_candidate_short_name = candidate_short_names_split[0]+" "+str(candidate_electoral_points_split[0]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]))):
   long_candidate_short_name = candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[2]+" "+str(candidate_electoral_points_split[2]))):
   long_candidate_short_name = candidate_short_names_split[2]+" "+str(candidate_electoral_points_split[2]);
  svg_file_width = svg_file_width + ( len(long_candidate_short_name) * 10 );
  outputsvgstring = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>
 <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"%s\" height=\"593\">
  <title>%s US presidential election results</title>
""" % (str(svg_file_width), electoral_year);
  statetextoutput = statetextoutput + """   <text id=\"DemL\" x=\"855\" y=\"392\">%s</text>
   <text id=\"RepL\" x=\"855\" y=\"425\">%s</text>
   <text id=\"TrdL\" x=\"855\" y=\"458\">%s</text>
  </g>
 <path id=\"lines\" d=\"M844,62l13,29M832,86l8,17M889,153l34,3M882,178l41,12M866,184l51 33M845,230l50,22M837,250l51,26M833,261l46,33M800,251l61,61\" stroke=\"#000000\" stroke-width=\"1.6\"/>
 <rect id=\"Dem\" x=\"828\" y=\"373\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Rep\" x=\"828\" y=\"406\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Trd\" x=\"828\" y=\"439\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <path id=\"frames\" fill=\"none\" stroke=\"#A9A9A9\" stroke-width=\"2\" d=\"M215,493v55l36,45 M0,425h147l68,68h85l54,54v46\"/>
</svg>""" % (candidate_short_names_split[0]+" "+str(candidate_electoral_points_split[0]), candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]), candidate_short_names_split[2]+" "+str(candidate_electoral_points_split[2]), candidate_colors_split[0], candidate_colors_split[1], candidate_colors_split[2]);
 if(len(candidate_short_names_split)==4):
  svg_file_width = 1020;
  long_candidate_short_name = candidate_short_names_split[0]+" "+str(candidate_electoral_points_split[0]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]))):
   long_candidate_short_name = candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[2]+" "+str(candidate_electoral_points_split[2]))):
   long_candidate_short_name = candidate_short_names_split[2]+" "+str(candidate_electoral_points_split[2]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[3]+" "+str(candidate_electoral_points_split[3]))):
   long_candidate_short_name = candidate_short_names_split[3]+" "+str(candidate_electoral_points_split[3]);
  svg_file_width = svg_file_width + ( len(long_candidate_short_name) * 10 );
  outputsvgstring = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>
 <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"%s\" height=\"593\">
  <title>%s US presidential election results</title>
""" % (str(svg_file_width), electoral_year);
  statetextoutput = statetextoutput + """   <text id=\"DemL\" x=\"855\" y=\"392\">%s</text>
   <text id=\"RepL\" x=\"855\" y=\"425\">%s</text>
   <text id=\"TrdL\" x=\"855\" y=\"458\">%s</text>
   <text id=\"FrhL\" x=\"855\" y=\"491\">%s</text>
  </g>
 <path id=\"lines\" d=\"M844,62l13,29M832,86l8,17M889,153l34,3M882,178l41,12M866,184l51 33M845,230l50,22M837,250l51,26M833,261l46,33M800,251l61,61\" stroke=\"#000000\" stroke-width=\"1.6\"/>
 <rect id=\"Dem\" x=\"828\" y=\"373\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Rep\" x=\"828\" y=\"406\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Trd\" x=\"828\" y=\"439\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Frh\" x=\"828\" y=\"472\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <path id=\"frames\" fill=\"none\" stroke=\"#A9A9A9\" stroke-width=\"2\" d=\"M215,493v55l36,45 M0,425h147l68,68h85l54,54v46\"/>
</svg>""" % (candidate_short_names_split[0]+" "+str(candidate_electoral_points_split[0]), candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]), candidate_short_names_split[2]+" "+str(candidate_electoral_points_split[2]), candidate_short_names_split[3]+" "+str(candidate_electoral_points_split[3]), candidate_colors_split[0], candidate_colors_split[1], candidate_colors_split[2], candidate_colors_split[3]);
 if(len(candidate_short_names_split)==5):
  svg_file_width = 1020;
  long_candidate_short_name = candidate_short_names_split[0]+" "+str(candidate_electoral_points_split[0]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]))):
   long_candidate_short_name = candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[2]+" "+str(candidate_electoral_points_split[2]))):
   long_candidate_short_name = candidate_short_names_split[2]+" "+str(candidate_electoral_points_split[2]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[3]+" "+str(candidate_electoral_points_split[3]))):
   long_candidate_short_name = candidate_short_names_split[3]+" "+str(candidate_electoral_points_split[3]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[4]+" "+str(candidate_electoral_points_split[4]))):
   long_candidate_short_name = candidate_short_names_split[4]+" "+str(candidate_electoral_points_split[4]);
  svg_file_width = svg_file_width + ( len(long_candidate_short_name) * 10 );
  outputsvgstring = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>
 <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"%s\" height=\"593\">
  <title>%s US presidential election results</title>
""" % (str(svg_file_width), electoral_year);
  statetextoutput = statetextoutput + """   <text id=\"DemL\" x=\"855\" y=\"392\">%s</text>
   <text id=\"RepL\" x=\"855\" y=\"425\">%s</text>
   <text id=\"TrdL\" x=\"855\" y=\"458\">%s</text>
   <text id=\"FrhL\" x=\"855\" y=\"491\">%s</text>
   <text id=\"FthL\" x=\"855\" y=\"524\">%s</text>
  </g>
 <path id=\"lines\" d=\"M844,62l13,29M832,86l8,17M889,153l34,3M882,178l41,12M866,184l51 33M845,230l50,22M837,250l51,26M833,261l46,33M800,251l61,61\" stroke=\"#000000\" stroke-width=\"1.6\"/>
 <rect id=\"Dem\" x=\"828\" y=\"373\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Rep\" x=\"828\" y=\"406\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Trd\" x=\"828\" y=\"439\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Frh\" x=\"828\" y=\"472\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Fth\" x=\"828\" y=\"505\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <path id=\"frames\" fill=\"none\" stroke=\"#A9A9A9\" stroke-width=\"2\" d=\"M215,493v55l36,45 M0,425h147l68,68h85l54,54v46\"/>
</svg>""" % (candidate_short_names_split[0]+" "+str(candidate_electoral_points_split[0]), candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]), candidate_short_names_split[2]+" "+str(candidate_electoral_points_split[2]), candidate_short_names_split[3]+" "+str(candidate_electoral_points_split[3]), candidate_short_names_split[4]+" "+str(candidate_electoral_points_split[4]), candidate_colors_split[0], candidate_colors_split[1], candidate_colors_split[2], candidate_colors_split[3], candidate_colors_split[4]);
 if(len(candidate_short_names_split)==6):
  svg_file_width = 1020;
  long_candidate_short_name = candidate_short_names_split[0]+" "+str(candidate_electoral_points_split[0]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]))):
   long_candidate_short_name = candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[2]+" "+str(candidate_electoral_points_split[2]))):
   long_candidate_short_name = candidate_short_names_split[2]+" "+str(candidate_electoral_points_split[2]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[3]+" "+str(candidate_electoral_points_split[3]))):
   long_candidate_short_name = candidate_short_names_split[3]+" "+str(candidate_electoral_points_split[3]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[4]+" "+str(candidate_electoral_points_split[4]))):
   long_candidate_short_name = candidate_short_names_split[4]+" "+str(candidate_electoral_points_split[4]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[5]+" "+str(candidate_electoral_points_split[5]))):
   long_candidate_short_name = candidate_short_names_split[5]+" "+str(candidate_electoral_points_split[5]);
  svg_file_width = svg_file_width + ( len(long_candidate_short_name) * 10 );
  outputsvgstring = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>
 <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"%s\" height=\"593\">
  <title>%s US presidential election results</title>
""" % (str(svg_file_width), electoral_year);
  statetextoutput = statetextoutput + """   <text id=\"DemL\" x=\"855\" y=\"392\">%s</text>
   <text id=\"RepL\" x=\"855\" y=\"425\">%s</text>
   <text id=\"TrdL\" x=\"855\" y=\"458\">%s</text>
   <text id=\"FrhL\" x=\"855\" y=\"491\">%s</text>
   <text id=\"FthL\" x=\"855\" y=\"524\">%s</text>
   <text id=\"SihL\" x=\"855\" y=\"557\">%s</text>
  </g>
 <path id=\"lines\" d=\"M844,62l13,29M832,86l8,17M889,153l34,3M882,178l41,12M866,184l51 33M845,230l50,22M837,250l51,26M833,261l46,33M800,251l61,61\" stroke=\"#000000\" stroke-width=\"1.6\"/>
 <rect id=\"Dem\" x=\"828\" y=\"373\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Rep\" x=\"828\" y=\"406\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Trd\" x=\"828\" y=\"439\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Frh\" x=\"828\" y=\"472\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Fth\" x=\"828\" y=\"505\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Sih\" x=\"828\" y=\"538\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <path id=\"frames\" fill=\"none\" stroke=\"#A9A9A9\" stroke-width=\"2\" d=\"M215,493v55l36,45 M0,425h147l68,68h85l54,54v46\"/>
</svg>
""" % (candidate_short_names_split[0]+" "+str(candidate_electoral_points_split[0]), candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]), candidate_short_names_split[2]+" "+str(candidate_electoral_points_split[2]), candidate_short_names_split[3]+" "+str(candidate_electoral_points_split[3]), candidate_short_names_split[4]+" "+str(candidate_electoral_points_split[4]), candidate_short_names_split[5]+" "+str(candidate_electoral_points_split[5]), candidate_colors_split[0], candidate_colors_split[1], candidate_colors_split[2], candidate_colors_split[3], candidate_colors_split[4], candidate_colors_split[5]);
 if(len(candidate_short_names_split)>=7):
  svg_file_width = 1020;
  long_candidate_short_name = candidate_short_names_split[0]+" "+str(candidate_electoral_points_split[0]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]))):
   long_candidate_short_name = candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[2]+" "+str(candidate_electoral_points_split[2]))):
   long_candidate_short_name = candidate_short_names_split[2]+" "+str(candidate_electoral_points_split[2]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[3]+" "+str(candidate_electoral_points_split[3]))):
   long_candidate_short_name = candidate_short_names_split[3]+" "+str(candidate_electoral_points_split[3]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[4]+" "+str(candidate_electoral_points_split[4]))):
   long_candidate_short_name = candidate_short_names_split[4]+" "+str(candidate_electoral_points_split[4]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[5]+" "+str(candidate_electoral_points_split[5]))):
   long_candidate_short_name = candidate_short_names_split[5]+" "+str(candidate_electoral_points_split[5]);
  if(len(long_candidate_short_name)<len(candidate_short_names_split[6]+" "+str(candidate_electoral_points_split[6]))):
   long_candidate_short_name = candidate_short_names_split[6]+" "+str(candidate_electoral_points_split[6]);
  svg_file_width = svg_file_width + ( len(long_candidate_short_name) * 10 );
  outputsvgstring = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>
 <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"%s\" height=\"593\">
  <title>%s US presidential election results</title>
""" % (str(svg_file_width), electoral_year);
  statetextoutput = statetextoutput + """   <text id=\"DemL\" x=\"855\" y=\"392\">%s</text>
   <text id=\"RepL\" x=\"855\" y=\"425\">%s</text>
   <text id=\"TrdL\" x=\"855\" y=\"458\">%s</text>
   <text id=\"FrhL\" x=\"855\" y=\"491\">%s</text>
   <text id=\"FthL\" x=\"855\" y=\"524\">%s</text>
   <text id=\"SihL\" x=\"855\" y=\"557\">%s</text>
   <text id=\"SehL\" x=\"855\" y=\"590\">%s</text>
  </g>
 <path id=\"lines\" d=\"M844,62l13,29M832,86l8,17M889,153l34,3M882,178l41,12M866,184l51 33M845,230l50,22M837,250l51,26M833,261l46,33M800,251l61,61\" stroke=\"#000000\" stroke-width=\"1.6\"/>
 <rect id=\"Dem\" x=\"828\" y=\"373\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Rep\" x=\"828\" y=\"406\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Trd\" x=\"828\" y=\"439\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Frh\" x=\"828\" y=\"472\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Fth\" x=\"828\" y=\"505\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Sih\" x=\"828\" y=\"538\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <rect id=\"Seh\" x=\"828\" y=\"571\" height=\"19\" width=\"19\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.8\"/>
 <path id=\"frames\" fill=\"none\" stroke=\"#A9A9A9\" stroke-width=\"2\" d=\"M215,493v55l36,45 M0,425h147l68,68h85l54,54v46\"/>
</svg>
""" % (candidate_short_names_split[0]+" "+str(candidate_electoral_points_split[0]), candidate_short_names_split[1]+" "+str(candidate_electoral_points_split[1]), candidate_short_names_split[2]+" "+str(candidate_electoral_points_split[2]), candidate_short_names_split[3]+" "+str(candidate_electoral_points_split[3]), candidate_short_names_split[4]+" "+str(candidate_electoral_points_split[4]), candidate_short_names_split[5]+" "+str(candidate_electoral_points_split[5]), candidate_short_names_split[6]+" "+str(candidate_electoral_points_split[6]), candidate_colors_split[0], candidate_colors_split[1], candidate_colors_split[2], candidate_colors_split[3], candidate_colors_split[4], candidate_colors_split[5], candidate_colors_split[6]);
 outputsvgstring = outputsvgstring + statemapoutput + statetextoutput;
 if(output_to_file==True):
  svgfile = open("ElectoralCollege"+electoral_year+".svg", "w")
  svgfile.write(outputsvgstring);
  svgfile.close();
  return True;
 if(output_to_file==False):
  return outputsvgstring;

def GenerateElectoralMapToPNG(electoral_year):
 outputsvg = GenerateElectoralMap(candidate_names, candidate_short_names, candidate_colors, candidate_electoral_points, winning_candidate_states, electoral_college_points, state_initials, electoral_year, False);
 if(outputsvg==False):
  return False;
 cairosvg.svg2png(bytestring=outputsvg.encode('utf-8'), write_to="ElectoralCollege"+electoral_year+".png");
 return True;