from Search import *
from ChannelAnalyser import *
from VideoAnalyser import *
from ThumbnailAnalyser import *
from Report import *
from Charts import *
import time
import os

start_time = time.time()
SearchTime=time.asctime( time.localtime(time.time()))

# dont use "/" or ":" in text
text = "india tech"
NumPages=1


parent_dir = "Images"
directory = str(text)+"/Thumbnails"
try:
    path = os.path.join(parent_dir, directory) 
    os.makedirs(path)  
except:
    pass
try:
    directory = str(text)+"/Charts"
    path = os.path.join(parent_dir, directory) 
    os.makedirs(path)  
except:
    pass




result = SearchResults(text,NumPages)
Channels = GetChannels(result)
Videos = GetVideos(result)
BarChannelAge(GetChannelAge(Channels),text)
BarChannelViews(GetChannelViews(Channels),text)
BarChannelSubscribers(GetChannelSubscribers(Channels),text)
BarChannelVideos(GetChannelVideos(Channels),text)
BarVideoAges(GetVideoAge(Videos),text)
BarVideoDuration(GetVideoDuration(Videos),text)
BarVideoViews(GetVideoViews(Videos),text)
data = {
    'Channel for kids': list(GetChannelForKids(Channels).values()),
    'Channel comment moderation': list(GetChannelCommentModeration(Channels).values()),
    'Video caption available': list(GetVideoCaption(Videos).values()),
    'Video has licensed content': list(GetVideoLicense(Videos).values()),
    'Video embeddable' : list(GetVideoEmbeddable(Videos).values()),
    'Video for kids' : list(GetVideoKids(Videos).values())
}
HorizontalBarOverview(data,text)
ScatLikesDislikes(GetVideoLikesDislikes(Videos),text)
ScatViewsLikes(GetVideoViewsLikes(Videos),text)
ScatViewsComments(GetVideoViewsComments(Videos),text)
HorizontalBarAll4(GetVideoAll4(Videos),text)

ChannelCount=GetChannelCount(Videos, Channels)
ChannelTopics=GetChannelTopics(Channels)
ChannelCategories=GetChannelCategories(Channels)
VideoTags=GetVideoTagsCount(Videos)
VideoTopics=GetVideoRelevantTopics(Videos)
VideoCategories=GetVideoCategories(Videos)
TableChannels(ChannelCount,ChannelTopics, ChannelCategories,text)
TableVideos( VideoTags, VideoTopics, VideoCategories,text)
GetThumnbailImages(Videos,text)
ThumbnailAnalysis=GetThumbnailAnalysis(Videos)
TableThumbnails(ThumbnailAnalysis,text)
NumChannel=len(ChannelCount)
NumVideo=0
for i in ChannelCount:
    NumVideo+=ChannelCount[i]
GetReport(text,NumPages,NumChannel,NumVideo,result['region'],SearchTime)

end_time = time.time()
print(end_time-start_time)