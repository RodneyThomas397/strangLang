from sys import *
import os

wikiLink = "https://github.com/RodneyThomas397/strangle/wiki/Versions"
print("Running Strangle V1.0.0")
print("Refer to the DOCS here for information: " + wikiLink)

tokens = []

def open_file(filename):
    data = open(filename + ".strangle", "r").read()
    return data

def lex(filecontents):
    tok = ""
    state = 0
    string = ""
    filecontents = list(filecontents)
    for char in filecontents:
        tok += char
        if tok == " ":
            if state == 0:
                tok = ""
            else:
                tok = " "
        elif tok == "\n":
            tok = ""
        elif tok.lower() == "mark" or tok == "MARK":
            tokens.append("PRINT")
            tok = ""
        elif tok == "\"":
            if state == 0:
                state = 1
            elif state == 1:
                tokens.append("STRING:" + string + "\"")
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            string += tok
            tok = ""
    return tokens
    #print(tokens)

def parse(toks):
    i = 0
    while(i < len(toks)):
        if toks[i] + " " + toks[i+1][0:6] == "PRINT STRING":
            print(toks[i+1][7:])
            i+=2

def run():
    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)

run()
