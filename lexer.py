# Check if no arguments are given - ignore for now #
# Removed - Call from another function #
# Could also read from a file #
# Change a little to work with numbers rather than single digit #

def lex(patterns, inputString):
    # Tokenize the input string #
    tokens = []
    i = 0
    stringLength = len(inputString)

    for i in range(stringLength):
        for regex, name in patterns:
            match = regex.match(inputString, i)
            if match:
                token = (name, match.group())
                tokens.append(token)

    return tokens

