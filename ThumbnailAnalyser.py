import urllib.request
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='your api-key here')


def GetThumnbailImages(Videos):
    count=1
    for i in Videos:
        try:
            url=Videos[i]['VideoThumbnailURL']
            urllib.request.urlretrieve(url, "Images/Thumbnails/"+str(count)+".jpg")
            count+=1
        except:
            print("Thumbnail not available for")
            print(i)
            print(Videos[i]['VideoTitle'])
            print(url)
            print("----------------------------------------------")

def analyze_image(url):
    a=app.tag_urls([url])
    s=a["outputs"][0]["data"]["concepts"]
    temp=[]
    for i in s:
        if i["value"]>0.5:
            temp.append(i["name"])
    return temp


def GetThumbnailAnalysis(Videos):
    Visuals={}
    for i in Videos:
        url=Videos[i]['VideoThumbnailURL']
        try:
            temp=analyze_image(url)
        except:
            print("Analysis not available for")
            print(i)
            print(Videos[i]['VideoTitle'])
            print(url)
            continue

        for tag in temp:
            if tag not in Visuals:
                Visuals[tag]=1
            else:
                Visuals[tag]+=1
    negatives=["man","woman","person"]

    for i in negatives:
        if i in Visuals:
            del Visuals[i]
    sort_Visuals = sorted(Visuals.items(), key=lambda x: x[1], reverse=True)
    Visuals={}
    for i in sort_Visuals:
        Visuals[i[0]]=i[1]

    return Visuals