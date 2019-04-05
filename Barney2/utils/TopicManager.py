
from utils.topics.GoodbyeTopic import GoodbyeTopic
from utils.topics.HowAreYouTopic import HowAreYouTopic
from utils.topics.HowCanIHelpTopic import HowCanIHelpTopic
from utils.topics.WeatherTopic import WeatherTopic
from utils.Sentence import Sentence

class TopicManager:

    topics = []
    topic = None


    def __init__(self):
        
        self.topics = []
        self.topics.append(HowAreYouTopic())
        self.topics.append(WeatherTopic())
        self.topics.append(GoodbyeTopic())
        self.topics.append(HowCanIHelpTopic())


    def getTopic(self):
        
        return self.topic


    def identfyNextTopic(self, lastSentence: Sentence):
        
        for topic in self.topics:
            if topic.isTopicRelavent(lastSentence):
                nextSentence = topic.getNextSentence(lastSentence)
                if nextSentence != None:
                    self.topic = topic
                    return nextSentence
            
            
        
        
        