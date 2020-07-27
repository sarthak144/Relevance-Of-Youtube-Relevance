import dateutil.parser
from datetime import date,timedelta
from IDS import *
from math import log10

def GetVideoAge(Videos):
    VideoAge = {"Under 1W": 0, "1W-1M": 0, "1M-6M": 0, "6M-1Y": 0, "1Y-2Y" : 0, "2Y-5Y" : 0, "5Y-10Y" : 0, "Above 10Y": 0, "Unavailable": 0}
    for i in Videos:
        if(Videos[i]['Date']=="Unavailable"):
            VideoAge["Unavailable"]+=1
            continue
        d = dateutil.parser.parse(Videos[i]['Date']).date()
        age = (date.today() - d) // timedelta(days=7)
        if(age<=0):
            VideoAge['Under 1W']+=1
        elif(age>=1 and age<5):
            VideoAge['1W-1M']+=1            
        elif(age>=5 and age<26):
            VideoAge["1M-6M"]+=1
        elif(age>=26 and age<52):
            VideoAge["6M-1Y"]+=1
        elif(age>=52 and age<104):
            VideoAge["1Y-2Y"]+=1
        elif(age>=104 and age<260):
            VideoAge["2Y-5Y"]+=1
        elif(age>=260 and age<520):
            VideoAge["5Y-10Y"]+=1
        elif(age>=520):
            VideoAge["Above 10Y"]+=1
    return VideoAge


def GetVideoDuration(Videos):
    VideoDuration = {"Under 1Min": 0, "1Min-2Min": 0, "2Min-5Min": 0, "5Min-10Min": 0, "10Min-30Min" : 0, "Above 30Min": 0, "Live" : 0, "Unavailable": 0}
    for i in Videos:
        Hours=0
        Minutes=0
        Seconds=0
        if(Videos[i]['VideoDuration']=="Unavailable"):
            VideoDuration["Unavailable"]+=1
            continue
        elif(Videos[i]['VideoDuration']=="P0D"):
            VideoDuration["Live"]+=1
            continue
        else:
            t = Videos[i]['VideoDuration']
            t=t[2:]
            HrEndIndex=0
            MinEndIndex=0
            SecEndIndex=0
            try:
                HrEndIndex=t.index('H')
                Hours=int(t[:HrEndIndex])
            except:
                Hours=0
                HrEndIndex=-1
            try:
                MinEndIndex=t.index('M')
                Minutes=int(t[HrEndIndex+1:MinEndIndex])
            except:
                Minutes=0
                MinEndIndex=HrEndIndex
            try:
                SecEndIndex=t.index('S')
                Seconds=int(t[MinEndIndex+1:SecEndIndex])
            except:
                Seconds=0
        
        if Hours>=1 or Minutes>=30:
            VideoDuration["Above 30Min"]+=1
        elif(Minutes>=10 and Minutes<30 ):
            VideoDuration["10Min-30Min"]+=1
        elif(Minutes>=5 and Minutes<10):
            VideoDuration["5Min-10Min"]+=1
        elif(Minutes>=2 and Minutes<5):
            VideoDuration["2Min-5Min"]+=1
        elif(Minutes>=1 and Minutes<2):
            VideoDuration["1Min-2Min"]+=1
        elif(Minutes<=0):
            VideoDuration["Under 1Min"]+=1
    return VideoDuration


def GetVideoDefinition(Videos):
    VideoDefinition={}
    for i in Videos:
        if Videos[i]['VideoDefinition'] not in VideoDefinition:
            VideoDefinition[Videos[i]['VideoDefinition']]=1
        else:
            VideoDefinition[Videos[i]['VideoDefinition']]+=1
    return VideoDefinition

def GetVideoCaption(Videos):
    VideoCaption = {"Yes": 0, "No": 0,"Unavailable": 0}
    for i in Videos:
        if Videos[i]['VideoCaption']=="Unavailable":
            VideoCaption["Unavailable"]+=1
        elif Videos[i]['VideoCaption']:
            VideoCaption["Yes"]+=1
        else:
            VideoCaption["No"]+=1
    return VideoCaption

def GetVideoLicense(Videos):
    VideoLicense = {"Yes": 0, "No": 0,"Unavailable": 0}
    for i in Videos:
        if Videos[i]['VideoLicense']=="Unavailable":
            VideoLicense["Unavailable"]+=1
        elif Videos[i]['VideoLicense']:
            VideoLicense["Yes"]+=1
        else:
            VideoLicense["No"]+=1
    return VideoLicense

def GetVideoEmbeddable(Videos):
    VideoEmbeddable = {"Yes": 0, "No": 0,"Unavailable": 0}
    for i in Videos:
        if Videos[i]['VideoEmbeddable']=="Unavailable":
            VideoEmbeddable["Unavailable"]+=1
        elif Videos[i]['VideoEmbeddable']:
            VideoEmbeddable["Yes"]+=1
        else:
            VideoEmbeddable["No"]+=1
    return VideoEmbeddable

def GetVideoKids(Videos):
    VideoKids = {"Yes": 0, "No": 0,"Unavailable": 0}
    for i in Videos:
        if Videos[i]['VideoKids']=="Unavailable":
            VideoKids["Unavailable"]+=1
        elif Videos[i]['VideoKids']:
            VideoKids["Yes"]+=1
        else:
            VideoKids["No"]+=1
    return VideoKids

def GetVideoViews(Videos):
    VideoViews = {"Under 10K": 0, "10K-100K": 0 , "100K-1M": 0, "1M-10M": 0, "10M-50M": 0, "50M-100M": 0, "100M-1B": 0, "Above 1B" : 0,  "Unavailable": 0}
    for i in Videos:
        if Videos[i]['VideoViews']=="Unavailable":
            VideoViews["Unavailable"]+=1
            continue
        views=int(Videos[i]['VideoViews'])
        if(views in range(0,10000)):
            VideoViews["Under 10K"]+=1
        elif(views in range(10000,100000)):
            VideoViews["10K-100K"]+=1
        elif(views in range(100000,1000000)):
            VideoViews["100K-1M"]+=1       
        elif(views in range(1000000,10000000)):
            VideoViews["1M-10M"]+=1   
        elif(views in range(10000000,50000000)):
            VideoViews["10M-50M"]+=1
        elif(views in range(50000000,100000000)):
            VideoViews["50M-100M"]+=1
        elif(views in range(100000000,1000000000)):
            VideoViews["100M-1B"]+=1
        elif(views>=1000000000):
            VideoViews["Above 1B"]+=1
    return VideoViews

def GetVideoRelevantTopics(Videos):
    VideoRelevantTopics = {}
    for i in Videos:
        if Videos[i]['VideoRelevantTopics']=="Unavailable":
            if "Unavailable" not in VideoRelevantTopics:
                VideoRelevantTopics["Unavailable"]=1
            else:
                VideoRelevantTopics["Unavailable"]+=1
        else:
            UniqueTopics=set(Videos[i]['VideoRelevantTopics'])
            UniqueTopics=list(UniqueTopics)
            for j in UniqueTopics:
                try:
                    if IDs[j] not in VideoRelevantTopics:
                        VideoRelevantTopics[IDs[j]]=1
                    else:
                        VideoRelevantTopics[IDs[j]]+=1
                except:
                    continue
    sort_VideoRelevantTopics = sorted(VideoRelevantTopics.items(), key=lambda x: x[1], reverse=True)
    VideoRelevantTopics={}
    for i in sort_VideoRelevantTopics:
        VideoRelevantTopics[i[0]]=i[1]
    
    return VideoRelevantTopics

def GetVideoCategories(Videos):
    VideoCategories = {}
    for i in Videos:
        if Videos[i]['VideoCategories']=="Unavailable":
            if "Unavailable" not in VideoCategories:
                VideoCategories["Unavailable"]=1
            else:
                VideoCategories["Unavailable"]+=1
        else:
            for j in Videos[i]['VideoCategories']:
                category=j
                StartIndex=category.index("/wiki/")
                StartIndex+=6
                category=category[StartIndex:]
                category=category.replace('_'," ")
                if category not in VideoCategories:
                    VideoCategories[category]=1
                else:
                    VideoCategories[category]+=1
    sort_VideoCategories = sorted(VideoCategories.items(), key=lambda x: x[1], reverse=True)
    VideoCategories={}
    for i in sort_VideoCategories:
        VideoCategories[i[0]]=i[1]
    return VideoCategories

def GetVideoTagsCount(Videos):
    VideoTagsCount={}
    for i in Videos:
        VideoTags=Videos[i]['VideoTags']
        s=str(VideoTags)
        s=s[1:-1]
        s=s.lower()
        s=s.replace("'", '')
        s=s.replace(",", '')
        slist=s.split()
        for i in slist:
            if i not in VideoTagsCount:
                VideoTagsCount[i]=1
            else:
                VideoTagsCount[i]+=1
    sort_VideoTagsCount = sorted(VideoTagsCount.items(), key=lambda x: x[1], reverse=True)
    VideoTagsCount={}
    for i in sort_VideoTagsCount:
        VideoTagsCount[i[0]]=i[1]
    return VideoTagsCount


def GetVideoLikesDislikes(Videos):
    zerolikes=0
    zerodislikes=0
    zeroboth=0
    unavailable=0
    available=0
    Likes=[]
    Dislikes=[]
    for i in Videos:
        try:
            available+=1
            likevalue=log10(int(Videos[i]['VideoLikes']))
            dislikevalue=log10(int(Videos[i]['VideoDislikes']))
            Likes.append(likevalue)
            Dislikes.append(dislikevalue)
        except:
            if Videos[i]['VideoLikes']=="Unavailable" or Videos[i]['VideoDislikes']=="Unavailable":
                unavailable+=1
            else:
                if(int(Videos[i]['VideoLikes'])==0 and int(Videos[i]['VideoDislikes'])==0):
                    zeroboth+=1
                elif(int(Videos[i]['VideoDislikes'])==0):
                    zerodislikes+=0
                else:
                    zerolikes+=1
    Exceptions=[available,unavailable,zeroboth,zerodislikes,zerolikes]


    return((Likes,Dislikes,Exceptions))

def GetVideoViewsLikes(Videos):
    zeroviews=0
    zerolikes=0
    zeroboth=0
    unavailable=0
    available=0
    Likes=[]
    Views=[]
    for i in Videos:
        try:
            available+=1
            likevalue=log10(int(Videos[i]['VideoLikes']))
            viewvalue=log10(int(Videos[i]['VideoViews']))
            Likes.append(likevalue)
            Views.append(viewvalue)
        except:
            if Videos[i]['VideoLikes']=="Unavailable" or Videos[i]['VideoViews']=="Unavailable":
                unavailable+=1
            else:
                if(int(Videos[i]['VideoLikes'])==0 and int(Videos[i]['VideoViews'])==0):
                    zeroboth+=1
                elif(int(Videos[i]['VideoViews'])==0):
                    zeroviews+=0
                else:
                    zerolikes+=1
    Exceptions=[available,unavailable,zeroboth,zeroviews,zerolikes]

    return((Views,Likes,Exceptions))

def GetVideoViewsComments(Videos):
    zeroviews=0
    zerocomments=0
    zeroboth=0
    unavailable=0
    available=0
    Comments=[]
    Views=[]
    for i in Videos:
        # print(Videos[i]['VideoComments'])
        try:
            available+=1
            commentvalue=log10(int(Videos[i]['VideoComments']))
            viewvaule=log10(int(Videos[i]['VideoViews']))
            Comments.append(commentvalue)
            Views.append(viewvaule)
        except:
            if Videos[i]['VideoComments']=="Unavailable" or Videos[i]['VideoViews']=="Unavailable":
                unavailable+=1
            else:
                if(int(Videos[i]['VideoComments'])==0 and int(Videos[i]['VideoViews'])==0):
                    zeroboth+=1
                elif(int(Videos[i]['VideoViews'])==0):
                    zeroviews+=0
                else:
                    zerocomments+=1
    Exceptions=[available,unavailable,zeroboth,zeroviews,zerocomments]
    return((Views,Comments,Exceptions))


def GetVideoAll4(Videos):
    data={}
    for i in Videos:
        Title=Videos[i]["VideoTitle"]
        Views=Videos[i]["VideoViews"]
        Likes=Videos[i]["VideoLikes"]
        Dislikes=Videos[i]["VideoDislikes"]
        Comments=Videos[i]["VideoComments"]
        data[Title]=[]
        if(Views!='Unavailable' and Views!='0'):
            data[Title].append(log10(int(Views)))
        else:
            data[Title].append(0)
        if(Likes!='Unavailable' and Likes!='0'):
            data[Title].append(log10(int(Likes)))
        else:
            data[Title].append(0)
        if(Dislikes!='Unavailable' and Dislikes!='0'):
            data[Title].append(log10(int(Dislikes)))
        else:
            data[Title].append(0)
        if(Comments!='Unavailable' and Comments!='0'):
            data[Title].append(log10(int(Comments)))
        else:
            data[Title].append(0)
    return data