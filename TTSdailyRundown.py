import requests
import gtts
from playsound import playsound
from datetime import datetime

def getWeatherData(lat, long):
    responseList = requests.get("https://api.open-meteo.com/v1/forecast?latitude="+str(lat)+"&longitude="+str(long)+"&current_weather=true&hourly=precipitation_probability")
    weatherList = responseList.json()
    precipitation = weatherList["hourly"]
    precipitation = precipitation["precipitation_probability"]
    weather = weatherList["current_weather"]
    return weather, precipitation

def getDegrees(weather):
    direction = "ERROR"
    degrees = float(weather["winddirection"])
    if degrees >= 337.5 or degrees <= 22.5:
        direction = "North"
    elif 22.5 < degrees < 67.5:
        direction = "North-East"
    elif 67.5 <= degrees <= 112.5:
        direction = "East"
    elif 112.5 < degrees < 157.5:
        direction = "South-East"
    elif 157.5 <= degrees <= 202.5:
        direction = "South"
    elif 202.5 < degrees < 247.5:
        direction = "South-West"
    elif 247.5 <= degrees <= 292.5:
        direction = "West"
    elif 292.5 < degrees < 337.5:
        direction = "North-West"
    return direction

def getWindSpeed(weather):
    windspeedkmh = float(weather["windspeed"])
    windspeedmph = int(windspeedkmh / 1.609)
    if windspeedmph < 1:
        windspeed = "Calm"
    elif 1 <= windspeedmph <= 3:
        windspeed = "Light Air"
    elif 4 <= windspeedmph <= 7:
        windspeed = "Light Breeze"
    elif 8 <= windspeedmph <= 12:
        windspeed = "Gentle Breeze"
    elif 13 <= windspeedmph <= 18:
        windspeed = "Moderate Breeze"
    elif 19 <= windspeedmph <= 24:
        windspeed = "Fresh Breeze"
    elif 25 <= windspeedmph <= 31:
        windspeed = "Strong Breeze"
    elif 32 <= windspeedmph <= 38:
        windspeed = "Near Gale"
    elif 39 <= windspeedmph <= 46:
        windspeed = "Gale"
    elif 47 <= windspeedmph <= 54:
        windspeed = "Strong Gale"
    elif 55 <= windspeedmph <= 63:
        windspeed = "Whole Gale"
    elif 64 <= windspeedmph <= 75:
        windspeed = "Storm Force"
    elif windspeedmph < 75:
        windspeed = "Hurricane Force"
    else:
        windspeed = "ERROR"
    return windspeed

def getHeat(weather):
    temperature = float(weather["temperature"])
    if temperature < 1 :
        heat = "Freezing"
    elif 1 <= temperature < 10:
        heat = "Cold"
    elif 10 <= temperature <= 16:
        heat = "Cool"
    elif 17 <= temperature <= 22:
        heat = "Warm"
    elif temperature > 22:
        heat = "Hot"
    else:
        heat = "N/A"
    return heat

def precipitationProbability(precipitation):
    total = 0
    count = 0
    for row in precipitation:
        total = total + float(row)
        count = count + 1
    avg = round(total / count, 2)
    return avg

def printWeather(weather, windspeed, direction, heat, location, preprob):
    global dailyRundown
    weatherSpeech = "Today the weather in "+str(location)+" is "+str(heat.lower())+" with a "+str(windspeed.lower())+". The temperature is "+str(weather["temperature"])+" degrees celsius, The Chance of Precipitation "+str(preprob)+", Windspeed "+str(weather["windspeed"])+" kilometers per hour and Wind Direction "+str(direction)+". "
    dailyRundown= dailyRundown+weatherSpeech


def weatherMain():
    coordinates = ["Tamworth", "52.63", "-1.69"],["Coventry", "52.40", "-1.49"]
    for row in coordinates:
        weather, precipitation = getWeatherData(row[1], row[2])
        preprob = precipitationProbability(precipitation)
        windspeed = getWindSpeed(weather)
        direction = getDegrees(weather)
        heat = getHeat(weather)
        printWeather(weather, windspeed, direction, heat, row[0], preprob)

def newsHeadlines():
    global dailyRundown
    responseList = requests.get("https://newsdata.io/api/1/news?apikey=pub_2571015de394b5ce77ef6b8ec0145429c45ad&q=neuroscience&language=en")
    newsList = responseList.json()
    newsList = newsList["results"]
    news = "Top neuroscience headlines of today are as follows. "
    for i in range(3):
        currentArticle = newsList[i]
        strNews = str(currentArticle["title"])+". "
        news = news + strNews
    dailyRundown = dailyRundown+news

def intro():
    global dailyRundown
    time = str(datetime.now())
    time = time[:len(time)-10]
    hello = "Hello Oliver. I hope you have a good day. The date and time is "+str(time)+". "
    dailyRundown = dailyRundown+hello

def bye():
    global dailyRundown
    bye = "Thanks for listening to your daily rundown"
    dailyRundown = dailyRundown+bye

global dailyRundown
dailyRundown = ""
intro()  
weatherMain()
newsHeadlines()
tts = gtts.gTTS(dailyRundown)
tts.save("dailyRundown.mp3")
playsound("dailyRundown.mp3")
