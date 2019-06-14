"""
tokenizer.py

Trent Schwartz

A java lexer class


"""
# TODO implement simpler version of sring tiling
# create github
import javac_parser
import os.path
import time
from collections import Counter


class tokenizer():
    """class tokenizer takes an input folder path, creates a tokenizer obj,
    and an output dictionary with each files lexed result held in a multidim
    string array"""

    def __init__(self, iff):
        self.outputDict = dict()
        self.inputFileFolder = iff
        self.summaryDict = dict()

    def folderRead(self):

        print(time.clock())
        java = javac_parser.Java()
        dirlist = os.listdir(self.inputFileFolder)
        if self.inputFileFolder[-1] is not "/":
            self.inputFileFolder = self.inputFileFolder + "/"
        for item in dirlist:
            if os.path.isfile(self.inputFileFolder + item):
                with open(str(self.inputFileFolder + item), 'r+') as ifile:
                    self.outputDict[int(item[:6])] = []
                    for line in ifile:
                        self.outputDict[int(item[:6])].extend(java.lex(line))
        for key in self.outputDict:
            self.outputDict[int(key)].append(
                self.summarize(self.outputDict[key]))
        print(time.clock())

    def summarize(self, tlist):
        c = Counter()
        for elem in tlist:
            c[elem[0]] += 1

        return c
