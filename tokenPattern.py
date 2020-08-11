import re
# All the token matching should be done here - Basic rules #

patterns = [
    (r'[0-9]+','INT'),
    (r'\(','LP'),
    (r'\)','RP'),
    (r'\,','COMA'),
    ('[A-Za-z]','CHAR')
]

patterns = [(re.compile(expr), name) for expr, name in patterns]
