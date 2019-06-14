"""
Tokenizer.py

A tokenization program
This implementation uses a deque

Trent Schwartz

jun 3 2019
"""

import re
import os.path
from collections import deque
from dataclasses import dataclass, field
from typing import Deque
from sly import Lexer


@dataclass
class tokenizer(Lexer):

    inputFile: str
    outputFile: str = field(default="replace")
    tokenCollector: Deque = field(default_factory=deque)
    whitespaceCollector: Deque
    token = {
            ID, DIGIT, PLUS, MINUS, MULT, DIVIDE, ASSIGN,
            LPAREN, RPAREN, LBRACKET, RBRACKET, LSHARP,
            RSHARP
            }

    ID = r'[a-zA-Z][a-zA-Z0-9]*'
    DIGIT = r'\d+'
    PLUS = r'\+'
    MINUS = r'-'
    MULT = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACKET = r'\{'
    RBRACKET = r'\}'
    LSHARP = r'<'
    RSHARP = r'>'

    ignore = ' \t'
    ignore_comment = r'//'
    ignore_mcomment = r'/\*'

    def __post_init__(self):

        if self.outputFile == "replace":

            self.outputFile = self.inputFile.split(
                "/")[-1][:-5] if os.path.exists(self.inputFile) else print(
                    "Error creating output file path, check input file path")

    def token(self, inputfile):
        ifiledata = ""
        with open(inputfile, 'r+') as ifile:
            for line in ifile:
                ifiledata.append(line)

        ifile.close()
        ifiledata.replace(" ", "")
        for tok in self.tokenize(ifiledata):
            tokenCollector.append(tok)


        
        





