
from utils.Topic import Topic
from utils.Direction import Direction
from utils.Sentence import Sentence
from utils.app.weather.OpenWeatherApp import OpenWeatherApp

class WeatherTopic(Topic):

    def isTopicRelavent(self, lastSentence: Sentence):
        return lastSentence.containsPhrase("WEATHER")
        

    def getNextSentenceFromLastSentence(self, lastSentence: Sentence):
 
        if lastSentence.containsPhrase("WEATHER"):
            return Sentence(Direction.OUT,self.getTomorrowsWeather())
        
        return None


    def getTomorrowsWeather(self):
        
        weatherApp = OpenWeatherApp()
        return weatherApp.getWeatherForTomorrow()
    
