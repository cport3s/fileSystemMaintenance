import os 
import datetime
import re
from time import gmtime, strftime

dateString = strftime("%d-%m-%Y", gmtime())
rootdir = ""
regex = re.compile(rf".*({dateString}).*$")

for root, dirs, files in os.walk(rootdir):
    for dir in dirs:
        if not regex.match(dir):
            os.rmdir(dir)
            # print(dir)