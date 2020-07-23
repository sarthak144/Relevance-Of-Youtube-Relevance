from apiclient.discovery import build
import urllib.request
from pandas import json_normalize
from json import dumps
# build will simply create the resource
# object in the Google API Python client
# which can be used to interact with any
# Google API
apikey=''
youtube = build('youtube', 'v3', developerKey=apikey)

# print(type(youtube))
# OUTPUT :: <class 'googleapiclient.discovery.Resource'>

# request = youtube.search().list(q='avengers', part='snippet', type='video', maxResults=50)
# 50 is the highest value per page
# print(type(request))
# OUTPUT :: <class 'googleapiclient.http.HttpRequest'>
# q is the query
# https://developers.google.com/youtube/v3/docs/search/list

# result = request.execute()
# print(result)
# print(type(result))
# OUTPUT :: <class 'dict'>
# print(type(result['items']))
# OUTPUT :: <class 'list'>
# print(type(result['items'][0]))
# OUTPUT :: <class 'dict'>
# for i in result:
#     print (i, end =" ")
#     # i is just the key => String
#     print(type(result[i]))
# OUTPUT ::
# kind <class 'str'>
# etag <class 'str'>
# nextPageToken <class 'str'>
# regionCode <class 'str'>
# pageInfo <class 'dict'>
# items <class 'list'>

# for i in result['items']:
#     print(i['snippet']['title'])
    # for printing the titles of all videos of first page
    # The result list will have first 50 items, the max number that can be on one page
NextPageToken=None
count=0
prevcount=1
# while(1):
#     request = youtube.search().list(q='iiitd', part='snippet', type='video', maxResults=50,pageToken= NextPageToken )
#     result = request.execute()
#     prevcount=count
#     for i in result['items']:
#         print(i['snippet']['title'])
#         count+=1
#     NextPageToken=result['nextPageToken']
#     print(NextPageToken)
#     print("--------------------------------------------")
#     if NextPageToken is None:
#         break

request = youtube.search().list(q='tech', part='snippet', type='video', maxResults=50,pageToken= NextPageToken )
result = request.execute()
for i in result['items']:
    print(dumps(responset=2))
    # print(result['items'][i])

# for i in result['items']:
#     urllib.request.urlretrieve(i['snippet']['thumbnails']['high']['url'], "Images/"+i['id']['videoId']+".jpg")
# print(result)

# print(count)
# print(result['nextPageToken'])


    
# {'kind': 'youtube#searchResult', 'etag': 'xFvOlaqjekUkPOru4qeAN_Q4_FY', 'id': {'kind': 'youtube#video', 'videoId': 'FkQeWwwQbWY'},
#  'snippet': {'publishedAt': '2020-01-29T12:30:00Z', 'channelId': 'UC0rpxsHBn1j3kBTtKJ_wQjQ', 'title': 'DTU vs IIIT DELHI Part - 2 | Choose Wisely | Shocking Facts about IIIT Delhi | Ft Tech Skool', 'description': 'Title - DTU vs IIIT DELHI | Choose Wisely | Shocking Facts about IIIT Delhi | Ft Tech Skool Want me to make a video on your topic? Fill this form and let me know ...', 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/FkQeWwwQbWY/default.jpg', 'width': 120, 'height': 90}, 'medium': {'url': 'https://i.ytimg.com/vi/FkQeWwwQbWY/mqdefault.jpg', 'width': 320, 'height': 180}, 'high': {'url': 'https://i.ytimg.com/vi/FkQeWwwQbWY/hqdefault.jpg', 'width': 480, 'height': 360}}, 'channelTitle': 'Harman Singh - Being IIITian', 'liveBroadcastContent': 'none', 'publishTime': '2020-01-29T12:30:00Z'}}

# -------------------------------------------------------------------------------------------------------
# SINGLE VIDEO DETAILS

request = youtube.videos().list(
    part="contentDetails,id,liveStreamingDetails,localizations,player,recordingDetails,snippet,statistics,status,topicDetails",
    id="H3Pmb3wyaEA"
)
response = request.execute()


print(dumps(response, indent=2))


# -------------------------------------------------------------------------------------------------------
# SINGLE CHANNEL DETAILS

request = youtube.channels().list(
    part="snippet, statistics, status, topicDetails, contentDetails,contentOwnerDetails,brandingSettings,id,localizations,invideoPromotion,brandingSettings",
    id="UC0rE2qq81of4fojo-KhO5rg"
)
response = request.execute()

print(dumps(response, indent=2))

# -------------------------------------------------------------------------------------------------------

# import youtube_transcript_api
# from youtube_transcript_api import YouTubeTranscriptApi


# video_id="f2wVimni5zU"
# response=YouTubeTranscriptApi.get_transcript(video_id)
# print(response)