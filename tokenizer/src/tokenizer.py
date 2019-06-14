"""
tokenizer.py

Trent Schwartz

A java lexer class


"""

import javac_parser
import os.path
import time
from collections import deque


class tokenizer():

    def __init__(self, iff):
        self.outputDict = dict()
        self.inputFileFolder = iff

    def folderRead(self):

        print(time.clock())
        java = javac_parser.Java()
        dirlist = os.listdir(self.inputFileFolder)
        if self.inputFileFolder[-1] is not "/":
            self.inputFileFolder = self.inputFileFolder + "/"
        for item in dirlist:
            if os.path.isfile(self.inputFileFolder + item):
                with open(str(self.inputFileFolder + item), 'r+') as ifile:
                    filetokens = deque([])
                    for line in ifile:
                        filetokens.append(java.lex(line))
                    self.outputDict[item[:6]] = filetokens
        print(time.clock())
