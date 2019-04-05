
from utils.Topic import Topic
from utils.Direction import Direction
from utils.Sentence import Sentence

class HowAreYouTopic(Topic):

    def getNextSentenceFromLastSentence(self, lastSentence: Sentence):
        
        if lastSentence == None:
            return Sentence(Direction.OUT,"Hello, how are you?")
        
        if lastSentence.containsPhrase("HOW ARE YOU"):
            self.isTopicOver = True
            return Sentence(Direction.OUT, "Not bad, so how can I help?")
        
        return None
    
