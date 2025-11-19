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
        self.tokenType = CONSTS.TK_NONE
        self.token = ''

    def close(self):
        self.fp.close()

    def getNextLine(self):
        pass

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


    def _Parse(self):
        pass


    def _ParseInt(self):
        pass


    def _ParseIdent(self):
        pass


    def _ParseString(self):
        pass