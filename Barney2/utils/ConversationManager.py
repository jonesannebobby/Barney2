
from utils.Sentence import Sentence
from utils.Direction import Direction
from utils.TopicManager import TopicManager

class ConversationManager:
    
    def __init__(self):
        
        self.sentences = []
        self.isConversationOver = False
        self.topics = []
        self.topicManager = TopicManager()
        
     
    def getLastSentence(self):
        if len(self.sentences) > 0:
            return self.sentences[-1]
      
        return None
        

    def getNextSentenceText(self):
        
        nextSentence = self.getNextSentence()
        self.isConversationOver = nextSentence.isConversationOver
        self.sentences.append(nextSentence)
        return nextSentence
        
        
    def getCurrentTopic(self):
        return self.topics[-1]
    
        
    def getNextSentence(self):
        
        nextSentence = self.getNextSentenceFromLastTopic()

        if nextSentence == None:
            nextSentence = self.topicManager.identfyNextTopic(self.getLastSentence())
            self.topics.append(self.topicManager.getTopic())
            
        return nextSentence
        
        
    def getNextSentenceFromLastTopic(self):
        if len(self.topics) > 0:
            lastTopic = self.topics[-1]
            if lastTopic.isTopicOver:
                return None
            return self.topics[-1].getNextSentence(self.getLastSentence())
        else:
            return None


    def saveAnswer(self, answerText):
        self.sentences.append(Sentence(Direction.IN, answerText))
    
 
 
    
