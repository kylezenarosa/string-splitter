import re

class TagManipulator():    
    def parse_string(self, tags, regex=""):
        result = []
        tags = tags.strip()

        tempResult = re.split( regex, tags )
        if( len(tempResult[0]) > 0 ):
            result = tempResult  

        return result