import re
"""
generate Regex in word base and combined it with white space
"""

class Regex_generator():
    def __init__(self,word):
        self.word = word
        self.regex_string = ""
        self.current_type = self.determine_char_type(self.word[0])
    def determine_char_type(self, char):
        if char.isnumeric():
            return "DIGIT"
        elif char.isalpha():
            return "CHARACTER"
        elif char.isspace():
            return "WHITESPACE"
        else:
            return "SPECIAL"
    def regex_appender(self,cur_type,idx):
        if cur_type == 'DIGIT':
            self.regex_string +=('\\d+')
        elif cur_type == 'CHARACTER':
            self.regex_string +=('\\w+')
        elif cur_type == 'WHITESPACE':
            self.regex_string +=('\\s+')
        else :
            self.regex_string += "["+ self.word[idx-1] + "]"
    def regex_maker(self):
        for idx, char in enumerate(self.word):
            """
            when ever the character type change then its call the regex appender.
            """
            if self.current_type != self.determine_char_type(char) or self.determine_char_type(char) == 'SPECIAL' and idx != 0:
                self.regex_appender(self.current_type,idx)
                # if idx == len(self.word)-1:
                #     self.regex_appender(self.determine_char_type(char),idx+1)
            if idx == len(self.word)-1 :
                self.regex_appender(self.determine_char_type(char),idx+1)
            self.current_type = self.determine_char_type(char)
        return self.regex_string