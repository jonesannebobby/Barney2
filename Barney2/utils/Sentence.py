class Sentence:

    wordsSpoken = ""
    isConversationOver = False
    
    def __init__(self, direction, wordsSpoken):
        self.direction = direction
        self.wordsSpoken = wordsSpoken

    def containsPhrase(self, phrase: str):
        return " " + phrase.upper() + " " in " " + self.wordsSpoken.upper() + " "
    
    

