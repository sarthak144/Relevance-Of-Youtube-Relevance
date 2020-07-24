import dateutil.parser
from IDS import *

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
            print("live")
            VideoDuration["Live"]+=1
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
