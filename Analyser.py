import dateutil.parser
from IDS import *


def GetChannelCount(Videos, Channels):
    ChannelCount = {}
    for i in Videos:
        if Channels[Videos[i]['ChannelID']]['ChannelTitle'] not in ChannelCount:
            ChannelCount[Channels[Videos[i]['ChannelID']]['ChannelTitle']]=1
        else:
            ChannelCount[Channels[Videos[i]['ChannelID']]['ChannelTitle']]+=1
    return ChannelCount

def GetChannelAge(Channels):
    ChannelAge = {"Under 1Y": 0, "1Y-2Y": 0, "2Y-5Y": 0, "5Y-10Y": 0, "Above 10Y": 0, "Unavailable": 0}
    for i in Channels:
        if(Channels[i]['ChannelAge']=="Unavailable"):
            ChannelAge["Unavailable"]+=1
            continue
        d = dateutil.parser.parse(Channels[i]['ChannelAge']).date()
        age = (date.today() - d) // timedelta(days=7)
        if(age<52):
            ChannelAge['Under 1Y']+=1
        elif(age<104 and age>52):
            ChannelAge["1Y-2Y"]+=1
        elif(age<260 and age>104):
            ChannelAge["2Y-5Y"]+=1
        elif(age<520 and age>260):
            ChannelAge["5Y-10Y"]+=1
        elif(age>520):
            ChannelAge["Above 10Y"]+=1
    return ChannelAge

def GetChannelCountry(Channels):
    ChannelCountries = {}
    for i in Channels:
        if Channels[i]['ChannelCountry'] not in ChannelCountries:
            ChannelCountries[Channels[i]['ChannelCountry']]=1
        else:
            ChannelCountries[Channels[i]['ChannelCountry']]+=1
    return ChannelCountries


def GetChannelViews(Channels):
    ChannelViews = {"Under 100K": 0, "100K-1M": 0, "1M-10M": 0, "10M-100M": 0, "100M-500M": 0, "500M-1B": 0, "Above 1B" : 0,  "Unavailable": 0}
    for i in Channels:
        if Channels[i]['ChannelViews']=="Unavailable":
            ChannelViews["Unavailable"]+=1
            continue
        views=int(Channels[i]['ChannelViews'])
        if(views in range(0,100000)):
            ChannelViews["Under 100K"]+=1
        elif(views in range(100000,1000000)):
            ChannelViews["100K-1M"]+=1       
        elif(views in range(1000000,10000000)):
            ChannelViews["1M-10M"]+=1   
        elif(views in range(10000000,100000000)):
            ChannelViews["10M-100M"]+=1
        elif(views in range(100000000,500000000)):
            ChannelViews["100M-500M"]+=1
        elif(views in range(500000000,1000000000)):
            ChannelViews["500M-1B"]+=1
        elif(views>=1000000000):
            ChannelViews["Above 1B"]+=1
    return ChannelViews

def GetChannelSubscribers(Channels):
    ChannelSubscribers = {"Under 10K": 0, "10K-100K": 0, "100K-1M" : 0, "1M-5M": 0, "5M-10M" : 0, "10M-25M": 0, "25M-50M": 0, "Above 50M" : 0,  "Unavailable": 0}
    for i in Channels:
        if Channels[i]['ChannelSubscribers']=="Unavailable":
            ChannelSubscribers["Unavailable"]+=1
            continue
        Subscribers=int(Channels[i]['ChannelSubscribers'])
        if(Subscribers in range(0,10000)):
            ChannelSubscribers["Under 10K"]+=1
        elif(Subscribers in range(10000,100000)):
            ChannelSubscribers["10K-100K"]+=1       
        elif(Subscribers in range(100000,1000000)):
            ChannelSubscribers["100K-1M"]+=1   
        elif(Subscribers in range(1000000,5000000)):
            ChannelSubscribers["1M-5M"]+=1
        elif(Subscribers in range(5000000,10000000)):
            ChannelSubscribers["5M-10M"]+=1
        elif(Subscribers in range(10000000,25000000)):
            ChannelSubscribers["10M-25M"]+=1
        elif(Subscribers in range(25000000,50000000)):
            ChannelSubscribers["25M-50M"]+=1
        elif(Subscribers>=50000000):
            ChannelSubscribers["Above 50M"]+=1
    return ChannelSubscribers


def GetChannelVideos(Channels):
    ChannelVideos = {"Under 50": 0, "50-100": 0, "100-250" : 0, "250-500": 0, "500-1000" : 0, "1000-2500": 0, "2500-5000": 0, "Above 5000" : 0,  "Unavailable": 0}
    for i in Channels:
        if Channels[i]['ChannelVideos']=="Unavailable":
            ChannelVideos["Unavailable"]+=1
            continue
        Videos=int(Channels[i]['ChannelVideos'])
        if(Videos in range(0,50)):
            ChannelVideos["Under 50"]+=1
        elif(Videos in range(50,100)):
            ChannelVideos["50-100"]+=1       
        elif(Videos in range(100,250)):
            ChannelVideos["100-250"]+=1   
        elif(Videos in range(250,500)):
            ChannelVideos["250-500"]+=1
        elif(Videos in range(500,1000)):
            ChannelVideos["500-1000"]+=1
        elif(Videos in range(1000,2500)):
            ChannelVideos["1000-2500"]+=1
        elif(Videos in range(2500,5000)):
            ChannelVideos["2500-5000"]+=1
        elif(Videos>=5000):
            ChannelVideos["Above 5000"]+=1
    return ChannelVideos


def GetChannelTopics(Channels):
    ChannelTopics = {}
    for i in Channels:
        if Channels[i]['ChannelTopics']=="Unavailable":
            if "Unavailable" not in ChannelTopics:
                ChannelTopics["Unavailable"]=1
            else:
                ChannelTopics["Unavailable"]+=1
        else:
            UniqueTopics=set(Channels[i]['ChannelTopics'])
            UniqueTopics=list(UniqueTopics)
            for j in UniqueTopics:
                if IDs[j] not in ChannelTopics:
                    ChannelTopics[IDs[j]]=1
                else:
                    ChannelTopics[IDs[j]]+=1
    
    return ChannelTopics

def GetChannelCategories(Channels):
    ChannelCategories = {}
    for i in Channels:
        if Channels[i]['ChannelCategories']=="Unavailable":
            if "Unavailable" not in ChannelCategories:
                ChannelCategories["Unavailable"]=1
            else:
                ChannelCategories["Unavailable"]+=1
        else:
            for j in Channels[i]['ChannelCategories']:
                category=j
                StartIndex=category.index("/wiki/")
                StartIndex+=6
                category=category[StartIndex:]
                category=category.replace('_'," ")
                if category not in ChannelCategories:
                    ChannelCategories[category]=1
                else:
                    ChannelCategories[category]+=1
    return ChannelCategories


def GetChannelForKids(Channels):
    ChannelForKids = {"Yes": 0, "No": 0,"Unavailable": 0}
    for i in Channels:
        if Channels[i]['ChannelKids']=="Unavailable":
            ChannelForKids["Unavailable"]+=1
        elif Channels[i]['ChannelKids']:
            ChannelForKids["Yes"]+=1
        else:
            ChannelForKids["No"]+=1
    
    return ChannelForKids

def GetChannelCommentModeration(Channels):
    ChannelCommentModeration = {"Yes": 0, "No": 0,"Unavailable": 0}
    for i in Channels:
        if Channels[i]['ChannelCommentModeration']=="Unavailable":
            ChannelCommentModeration["Unavailable"]+=1
        elif Channels[i]['ChannelCommentModeration']:
            ChannelCommentModeration["Yes"]+=1
        else:
            ChannelCommentModeration["No"]+=1
    
    return ChannelCommentModeration


