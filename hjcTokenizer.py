import hjcConstants as CONSTS

class Tokenizer(object):
    def __init__(self, sourceName):
        """
        Open 'sourceFile' and gets ready to parse it.
        """
        self.sourceFileName = sourceName
        self.fp = open(sourceName, 'r');
        self.lineNumber = 0
        self.line = ''
        self.rawline = ''
        self.inComment = False
        # Initialize other varibles here
<<<<<<< HEAD
        self.tokenType = CONSTS.TK_NONE
        self.token = ''

=======

        #token info
        self.tokenType = CONSTS.TK_NONE
        self.token = '' #raw token text (string, int as string)
>>>>>>> Racheldev
    def close(self):
        self.fp.close()

    def getNextLine(self):
<<<<<<< HEAD
        pass
=======
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
>>>>>>> Racheldev

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
<<<<<<< HEAD
        while True:
            # if the current line is empty, get a new one
            if not self.line:
                if not self.getNextLine():
                    # end of file
                    self.tokenType = CONSTS.TK_NONE
                    self.token = ''
                    return False
                    
            # if we are inside a block comment, skip until */
            if self.inComment:
                end = self.line.find('*/')
                if end == -1:
                    # skip the entire line
                    self.line = ''
                    continue
                else:
                    # end of comment on this line
                    self.line = self.line[end+2:]
                    self.inComment = False
                    # loop again
                    continue
            # skip leading whitespace
            while self.line and self.line[0].isspace():
                self._eat()
            if not self.line:
                continue # line was only whitespace, skip
            #line now starts at a non-whitespace character
            if self.line .startswith('/**'):
                # doc style block comment
                self.inComment = True
                self.line = self.line[3:]
                continue
            elif self.line .startswith('/*'):
                # normal block comment
                self.inComment = True
                self.line = self.line[2:]
                continue
            elif self.line .startswith('//'):
                # line comment, skip rest of line
                self.line = ''
                continue
            break # got a non-comment, non-whitespace line
        
            
            
            
    def LineNumber(self):
        pass


    def LineStr(self):
        pass


    def TokenType(self):
        pass


    def TokenTypeStr(self):
        pass


    def Keyword(self):
        pass


    def KeywordStr(self, keywordId=None):
        pass


    def Symbol(self):
        pass


    def Identifier(self):
        pass


    def IntVal(self):
        pass


    def StringVal(self):
        pass
=======
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

>>>>>>> Racheldev


    def _Parse(self):
        pass


    def _ParseInt(self):
        pass


    def _ParseIdent(self):
        pass


    def _ParseString(self):
        pass