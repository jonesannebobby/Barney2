
from utils.Topic import Topic
from utils.Direction import Direction
from utils.Sentence import Sentence

class WeatherTopic(Topic):

    def isTopicRelavent(self, lastSentence: Sentence):
        return lastSentence.containsPhrase("WEATHER")
        

    def getNextSentenceFromLastSentence(self, lastSentence: Sentence):
 
        if lastSentence.containsPhrase("WEATHER"):
            return Sentence(Direction.OUT,"The weather tomorrow will be Sunny and showers")
        
        return None
        