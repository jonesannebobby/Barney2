
from utils.Topic import Topic
from utils.Direction import Direction
from utils.Sentence import Sentence

class GoodbyeTopic(Topic):

    def isTopicRelavent(self, lastSentence: Sentence):
        return lastSentence.containsPhrase("BYE")
    
    
    def getNextSentenceFromLastSentence(self, lastSentence: Sentence):
 
        nextSentence = Sentence(Direction.OUT,"OK, See you soon")
        nextSentence.isConversationOver = True
        return nextSentence
    
