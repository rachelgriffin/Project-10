import hjcConstants as CONSTS

class Tokenizer(object):
    def __init__(self, sourceName):
        """
        Open 'sourceFile' and gets ready to parse it.
        """
        self.sourceFileName = sourceName
        self.fp = open(sourceName, 'r')
        self.lineNumber = 0
        self.line = ''
        self.rawline = ''
        self.inComment = False
        # Initialize other varibles here

        #token info
        self.tokenType = CONSTS.TK_NONE
        self.token = '' #raw token text (string, int as string)
    def close(self):
        self.fp.close()

    def getNextLine(self):
        """
        reads the next line from file into self.line/self.rawline
        """
        self.rawline = self.fp.readline()
        if not self.rawline:
            self.line = ''
            return False
        
        self.lineNumber += 1 
        #keep whitespace and just strip newline chars
        self.line = self.rawline.rstrip('\r\n')
        return True

    def _eat(self):
        """
        'Eats' the frontmost character of self.line
        """
        self.line = self.line[1:]

    def Advance(self):
        """
        Reads the next command from the input and makes it the current
        command.
        Returns True if a command was found, False at end of file.
        """
        pass
    #kelly doing

    def LineNumber(self):
        return self.lineNumber

    def LineStr(self):
        return self.rawline.rstrip('\r\n')
        #original line text without newline chars

    def TokenType(self):
        return self.tokenType


    def TokenTypeStr(self):
        mapping = {
            CONSTS.TK_NONE: 'NONE',
            CONSTS.TK_KEYWORD: 'KEYWORD',
            CONSTS.TK_SYMBOL: 'SYMBOL',
            CONSTS.TK_IDENTIFIER: 'IDENTIFIER',
            CONSTS.TK_INT_CONST: 'INT_CONST',
            CONSTS.TK_STRING_CONST: 'STRING_CONST'
        }
        return mapping.get(self.tokenType, 'UNKNOWN')
    
    def Keyword(self):
        "return the keyword string for the current token" #assume current token type is TK_KEYWORD
        if self.tokenType != CONSTS.TK_KEYWORD:
            raise ValueError('Keyword() called but current token isnt a keyword')
        else:
            return self.token 


    def KeywordStr(self, keywordId=None):
        """if keywordID is None, return the current keyword string otherwise, map an index to CONSTS.keywords"""
        if keywordId is None:
            return self.Keyword()
        else:
            return CONSTS.keywords[keywordId]


    def Symbol(self):
        if self.tokenType != CONSTS.TK_SYMBOL:
            raise ValueError('symbol() called but current token is not a symbol')
        else:
            return self.token


    def Identifier(self):
        if self.tokenType != CONSTS.TK_IDENTIFIER:
            raise ValueError('identifier() called but current token is not an identifier')
        else:
            return self.token


    def IntVal(self):
        if self.tokenType != CONSTS.TK_INT_CONST:
            raise ValueError('IntVal() called but current token is not an IntVal')
        else:
            return int(self.token)

    def StringVal(self):
        if self.tokenType != CONSTS.TK_STRING_CONST:
            raise ValueError('StringVal() called but current token is not an stringVal')
        else:
            return self.token



    def _Parse(self):
        pass


    def _ParseInt(self):
        pass


    def _ParseIdent(self):
        pass


    def _ParseString(self):
        pass