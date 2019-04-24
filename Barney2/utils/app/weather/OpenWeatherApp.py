
import requests
import json

class OpenWeatherApp(object):

    def __init__(self):

        self.mainUrl = 'http://api.openweathermap.org/data/2.5/forecast'
        self.appId = 'f22ea03693f078af7ab87f7f9260a434'
        self.location = 'welwyn,uk'
        

    def callWebServer(self):

        send_url = self.mainUrl + '?q=' + self.location + '&APPID=' + self.appId
        r = requests.get(send_url)
        j = json.loads(r.text)
        
        return j
    
    def getWeatherForTomorrow(self):
        
        j = self.callWebServer()
        return j['list'][3]['weather'][0]['description']
    

        