from abc import abstractmethod
from utils.Sentence import Sentence


class Topic:

    def __init__(self):
        self.sentences = []
        self.isTopicOver = False
        
    def saveSentence(self, sentence):
        self.sentences.append(sentence)
        
    def isTopicRelavent(self, lastSentence: Sentence):
        return True
        
        
    @abstractmethod
    def getNextSentenceFromLastSentence(self, lastSentence: Sentence):
        pass
    
   
    def getNextSentence(self, lastSentence: Sentence):
        
        nextSentence = self.getNextSentenceFromLastSentence(lastSentence)
        
        if nextSentence != None:
            self.saveSentence(lastSentence)
            self.saveSentence(nextSentence)
            return nextSentence
        
        else:
            return None
    
        