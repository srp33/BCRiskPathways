import os, sys
from utilities import *

inFilePath = sys.argv[1]
queryText = sys.argv[2]

fileText = readTextFromFile(inFilePath)

print queryText in fileText
