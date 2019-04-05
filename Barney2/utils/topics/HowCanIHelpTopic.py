
from utils.Topic import Topic
from utils.Direction import Direction
from utils.Sentence import Sentence

class HowCanIHelpTopic(Topic):

    def getNextSentenceFromLastSentence(self, lastSentence: Sentence):
 
        self.isTopicOver = True
        if len(self.sentences) > 0:
            return Sentence(Direction.OUT,"Can I help with anything else?")
        
        
        return Sentence(Direction.OUT,"How can I help?")
        
    
