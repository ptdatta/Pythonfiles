import requests
import json

def speak(str):
     from win32com.client import Dispatch
     speak=Dispatch("SAPI.SpVoice")
     speak.Speak(str)


if __name__=='__main__':
     speak("news for today..let's begin")
     url="https://newsapi.org/v2/top-headlines?country=in&apiKey=3c2542cd79e346a2a671014fcf2460f4"
     news=requests.get(url).text
     news_dict=json.loads(news)
     arts=news_dict['articles']
     for i in arts:
          speak(i['title'])
          speak("next news .. listen carefully")