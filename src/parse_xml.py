import pandas as pd
import numpy as np
import os
import glob
import pickle
from collections import Counter
import re
import csv
import xml.etree.ElementTree as ET

listofdata = []


def parse_xml(folder):
	""" 
	This opens each individual xml file and parses the information listed below into one big 	list.
 	    
	"""
    for x in glob.glob(folder + '/*.xml'):
        with open(x, 'rt', encoding='ISO-8859-1') as infile:
            tree = ET.parse(infile)
            for node in tree.iter():
                if node.tag == 'rootTag':
                    listofdata.append('rootTag')
                elif node.tag == 'AwardEffectiveDate':
                    listofdata.append(node.text)
                elif node.tag == 'AwardExpirationDate':
                    listofdata.append(node.text)
                elif node.tag == 'AwardAmount':
                    listofdata.append(node.text)
                elif node.tag == 'LongName':
                    listofdata.append(node.text)
                elif node.tag == 'AbstractNarration':
                    listofdata.append(node.text)
                elif node.tag == 'MinAmdLetterDate':
                    listofdata.append(node.text)
                elif node.tag == 'MaxAmdLetterDate':
                    listofdata.append(node.text)
                elif node.tag == 'StartDate':
                    listofdata.append(node.text)
                elif node.tag == 'Name':
                    listofdata.append(node.text)
                elif node.tag == 'StateName':
                    listofdata.append(node.text)
                else:
                    pass        
    return listofdata


def separate_records(listofdata):
	"""
	This function breaks down giant list into separate rows for each individual record.

	"""

	roottag = re.compile(r'rootTag')
	rtlist=[]
	for i,v in enumerate(listofdata):
    		if re.match(roottag, str(v)):
        	rtlist.append(i)

	listofrecords = []	
	ind = 1
	for r in rtlist:
    		single_record = listofdata[r:rtlist[ind+1]]
    		listofrecords.append(single_record)
    		if ind < len(rtlist)-2:
        		ind += 1
    		else:
        		break
    
	return listofrecords



with open('listofrecords.pickle', 'wb') as f:
    pickle.dump(listofrecords, f)
