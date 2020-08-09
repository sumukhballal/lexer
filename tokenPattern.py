
# All the token matching should be done here - Basic rules #

pattern = [
    (r'[0-9]+','INT'),
    (r'\(','LP'),
    (r'\)','RP'),
    (r'\,','COMA'),
    ('[A-Za-z]','CHAR')
]