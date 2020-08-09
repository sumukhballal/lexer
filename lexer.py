import re
import sys

# Check if no arguments are given - ignore for now #
# Removed - Call from another function #
# Could also read from a file #
# Change a little to work with numbers rather than single digit #

def lex(tokenPattern,inputString):
    # Tokenize the input string #
    tokens=[]
    i=0
    stringLength=len(inputString)

    for i in range(0,stringLength):
        for tokenpattern in tokenPattern:
            pattern,tag=tokenpattern
            if re.compile(pattern).match(inputString,i):
                token="(\""+tag+"\","+"\""+inputString[i]+"\")"
                tokens.append(token)

    return tokens

