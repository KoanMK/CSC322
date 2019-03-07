import re

class Tokenizer:
    def __init__(self, input):
        self.index = 0
        self.tokens = re.findall("A[1-9][0-9]*|&|v|~|->|\(|\)", input)
    
    def next_token(self):
        try:
            self.index +=1
            return self.tokens[self.index-1]
        except IndexError:
            return None
