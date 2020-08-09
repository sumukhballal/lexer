import sys
import lexer
import tokenPattern

if __name__=='__main__':
    # Test run #
    testString="(1,5,10, 40, 50, 75,a)"
    tokens=lexer.lex(tokenPattern.pattern,testString)
    print(tokens)