from apiclient.discovery import build
import urllib.request

apikey='your api-key here'
youtube = build('youtube', 'v3', developerKey=apikey)


def SearchResults(text,NumPages):
    result={'items':[],'region':''}
    NextPageToken= None
    for i in range(NumPages):

        request = youtube.search().list(q=text, part='snippet', type='video', maxResults=50,pageToken= NextPageToken )
        resulttemp = request.execute()
        NextPageToken=resulttemp["nextPageToken"]
        result['items']+=resulttemp['items']
        try:
            result["region"]=resulttemp['regionCode']
        except:
            continue

    # print(dumps(result,indent=2))
    return result


def GetChannels(result):
    Channels={}
    for i in result['items']:
        Channels[i['snippet']['channelId']]={}
    for i in Channels:
        request = youtube.channels().list(
        part="snippet, statistics, status, topicDetails,brandingSettings,id,brandingSettings",
        id=i)
        response = request.execute()

        Channels[i]['ChannelTitle']=response['items'][0]['snippet']['title']
        Channels[i]['ChannelDescription']=response['items'][0]['snippet']['description']

        try:
            Channels[i]['ChannelCountry']=response['items'][0]['snippet']['country']
        except:
            Channels[i]['ChannelCountry']="Unavailable"

        Channels[i]['ChannelAge']=response['items'][0]['snippet']['publishedAt']
        Channels[i]['ChannelViews']=response['items'][0]['statistics']['viewCount']
        Channels[i]['ChannelSubscribers']=response['items'][0]['statistics']['subscriberCount']
        Channels[i]['ChannelVideos']=response['items'][0]['statistics']['videoCount']

        try:
            Channels[i]['ChannelTopics']=response['items'][0]['topicDetails']['topicIds']
        except:
            Channels[i]['ChannelTopics']="Unavailable"

        try:
            Channels[i]['ChannelCategories']=response['items'][0]['topicDetails']['topicCategories']
        except:
            Channels[i]['ChannelCategories']="Unavailable"

        try:
            Channels[i]['ChannelKids']=response['items'][0]['status']['madeForKids']
        except:
            Channels[i]['ChannelKids']="Unavailable"

        try:      
            Channels[i]['ChannelCommentModeration']=response['items'][0]['brandingSettings']['moderateComments']
        except:
            Channels[i]['ChannelCommentModeration']="Unavailable"
    return Channels


def GetVideos(result):
    Videos={}
    for i in result['items']:
        Videos[i['id']['videoId']]={}
    for i in Videos:
        request = youtube.videos().list(
        part="contentDetails,id,snippet,statistics,status,topicDetails",
        id=i)
        response = request.execute()
        if(response['items']!=[]):
            try:
                Videos[i]['Date']=response['items'][0]['snippet']['publishedAt']
            except:
                Videos[i]['Date']="Unavailable"
                # print("video date")
                # print(response['items'])
                # print(i)
            try:
                Videos[i]['ChannelID']=response['items'][0]['snippet']['channelId']
            except:
                Videos[i]['ChannelID']="Unavailable"
                # print("Video channel id")
                # print(response['items'])
                # print(response)
            try:
                Videos[i]['VideoTitle']=response['items'][0]['snippet']['title']
            except:
                Videos[i]['VideoTitle']="Unavailable"
            try:
                Videos[i]['VideoDescription']=response['items'][0]['snippet']['description']
            except:
                Videos[i]['VideoDescription']="Unavailable"

            try:
                Videos[i]['VideoThumbnailURL']=response['items'][0]['snippet']['thumbnails']['high']['url']
            except:
                try:
                    Videos[i]['VideoThumbnailURL']=response['items'][0]['snippet']['thumbnails']['default']['url']
                except:
                    Videos[i]['VideoThumbnailURL']="Unavailable"
            try:
                Videos[i]['VideoTags']=response['items'][0]['snippet']['tags']
            except:
                Videos[i]['VideoTags']="Unavailable"
            try:
                Videos[i]['VideoDuration']=response['items'][0]['contentDetails']['duration']
            except:
                Videos[i]['VideoDuration']="Unavailable"
            try:
                Videos[i]['VideoDefinition']=response['items'][0]['contentDetails']['definition']
            except:
                Videos[i]['VideoDefinition']="Unavailable"
            try:
                Videos[i]['VideoCaption']=response['items'][0]['contentDetails']['caption']
            except:
                Videos[i]['VideoCaption']="Unavailable"
            try:
                Videos[i]['VideoLicense']=response['items'][0]['contentDetails']['licensedContent']
            except:
                Videos[i]['VideoLicense']="Unavailable"
            try:
                Videos[i]['VideoEmbeddable']=response['items'][0]['status']['embeddable']
            except:
                Videos[i]['VideoEmbeddable']="Unavailable"
            try:
                Videos[i]['VideoKids']=response['items'][0]['status']['madeForKids']
            except:
                Videos[i]['VideoKids']="Unavailable"
            try:
                Videos[i]['VideoViews']=response['items'][0]['statistics']['viewCount']
            except:
                Videos[i]['VideoViews']="Unavailable"

            try:
                Videos[i]['VideoLikes']=response['items'][0]['statistics']['likeCount']
            except:
                Videos[i]['VideoLikes']="Unavailable"

            try:
                Videos[i]['VideoDislikes']=response['items'][0]['statistics']['dislikeCount']
            except:
                Videos[i]['VideoDislikes']="Unavailable"

            try:
                Videos[i]['VideoComments']=response['items'][0]['statistics']['commentCount']
            except:
                Videos[i]['VideoComments']="Unavailable"

            try:
                Videos[i]['VideoRelevantTopics']=response['items'][0]['topicDetails']['relevantTopicIds']
            except:
                Videos[i]['VideoRelevantTopics']="Unavailable"

            try:
                Videos[i]['VideoCategories']=response['items'][0]['topicDetails']['topicCategories']
            except:
                Videos[i]['VideoCategories']="Unavailable"
    return Videos

