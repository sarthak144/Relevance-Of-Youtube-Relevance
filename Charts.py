import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def BarChannelAge(data,text):
    xtags = list(data.keys()) 
    yvalues = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(xtags, yvalues, color ='red',  width = 0.4)
    plt.xlabel("Age of channels")
    plt.ylabel("Number of channels")
    plt.title("Age of channels in top search results")
    for x,y in zip(xtags,yvalues):
        label = format(y)
        plt.annotate(label, # Lable on top of the bar
                    (x,y), # the coordinated of label
                    textcoords="offset points", # how to position the text
                    xytext=(0,3), # distance from text to points (x,y)
                    ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_BarChannelAge"))
    # plt.show()

def BarChannelViews(data,text):
    xtags = list(data.keys()) 
    yvalues = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(xtags, yvalues, color ='red',  width = 0.4)
    plt.xlabel("Views of channels")
    plt.ylabel("Number of channels")
    plt.title("View count of channels in top search results")
    for x,y in zip(xtags,yvalues):
        label = format(y)
        plt.annotate(label, # Lable on top of the bar
                    (x,y), # the coordinated of label
                    textcoords="offset points", # how to position the text
                    xytext=(0,3), # distance from text to points (x,y)
                    ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_BarChannelViews"))
    # plt.show()

def BarChannelSubscribers(data,text):
    xtags = list(data.keys()) 
    yvalues = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(xtags, yvalues, color ='red',  width = 0.4)
    plt.xlabel("Number of subscribers of channels")
    plt.ylabel("Number of channels")
    plt.title("Subscriber count of channels in top search results")
    for x,y in zip(xtags,yvalues):
        label = format(y)
        plt.annotate(label, # Lable on top of the bar
                    (x,y), # the coordinated of label
                    textcoords="offset points", # how to position the text
                    xytext=(0,3), # distance from text to points (x,y)
                    ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_BarChannelSubscribers"))
    # plt.show()

def BarChannelVideos(data,text):
    xtags = list(data.keys()) 
    yvalues = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(xtags, yvalues, color ='red',  width = 0.4)
    plt.xlabel("Number of videos of channels")
    plt.ylabel("Number of channels")
    plt.title("Video count of channels in top search results")
    for x,y in zip(xtags,yvalues):
        label = format(y)
        plt.annotate(label, # Lable on top of the bar
                    (x,y), # the coordinated of label
                    textcoords="offset points", # how to position the text
                    xytext=(0,3), # distance from text to points (x,y)
                    ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_BarChannelVideos"))
    # plt.show()

def BarVideoAges(data,text):
    xtags = list(data.keys()) 
    yvalues = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(xtags, yvalues, color ='red',  width = 0.4)
    plt.xlabel("Age of videos")
    plt.ylabel("Number of videos")
    plt.title("Age of videos in top search results")
    for x,y in zip(xtags,yvalues):
        label = format(y)
        plt.annotate(label, # Lable on top of the bar
                    (x,y), # the coordinated of label
                    textcoords="offset points", # how to position the text
                    xytext=(0,3), # distance from text to points (x,y)
                    ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_BarVideoAges"))
    # plt.show()

def BarVideoDuration(data,text):
    xtags = list(data.keys()) 
    yvalues = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(xtags, yvalues, color ='red',  width = 0.4)
    plt.xlabel("Length of videos")
    plt.ylabel("Number of videos")
    plt.title("Length of videos in top search results")
    for x,y in zip(xtags,yvalues):
        label = format(y)
        plt.annotate(label, # Lable on top of the bar
                    (x,y), # the coordinated of label
                    textcoords="offset points", # how to position the text
                    xytext=(0,3), # distance from text to points (x,y)
                    ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_BarVideoDuration"))
    # plt.show()

def BarVideoViews(data,text):
    xtags = list(data.keys()) 
    yvalues = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(xtags, yvalues, color ='red',  width = 0.4)
    plt.xlabel("Views of videos")
    plt.ylabel("Number of videos")
    plt.title("Views of videos in top search results")
    for x,y in zip(xtags,yvalues):
        label = format(y)
        plt.annotate(label, # Lable on top of the bar
                    (x,y), # the coordinated of label
                    textcoords="offset points", # how to position the text
                    xytext=(0,3), # distance from text to points (x,y)
                    ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_BarVideoViews"))
    # plt.show()

def HorizontalBarOverview(data,text):
    # data = {
    # 'Channel for kids': list(GetChannelForKids(Channels).values()),
    # 'Channel comment moderation': list(GetChannelCommentModeration(Channels).values()),
    # 'Video caption available': list(GetVideoCaption(Videos).values()),
    # 'Video has licensed content': list(GetVideoLicense(Videos).values()),
    # 'Video embeddable' : list(GetVideoEmbeddable(Videos).values()),
    # 'Video for kids' : list(GetVideoKids(Videos).values())
    # }
    category_names = ['Yes', 'No', 'Unavailable']

    labels = list(data.keys())
    channelcount=data['Channel for kids']
    sumchannel=0
    for i in channelcount:
        sumchannel+=i
    videocount=data['Video for kids']
    sumvideo=0
    for i in videocount:
        sumvideo+=i
    data = np.array(list(data.values()))
    data_cum = data.cumsum(axis=1)

    category_colors=['#00ff00','#ff4d4d','lightgrey']

    fig, ax = plt.subplots(figsize=(20, 15))
    ax.invert_yaxis()

    ax.set_xlim(0, np.sum(data, axis=1).max())
    plt.title("Various aspects of top search results \n (Results from "+str(sumchannel)+" channels and "+str(sumvideo)+" videos)", x=0.35,y=1.04)
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2

        for y, (x, c) in enumerate(zip(xcenters, widths)):
            if int(c)!=0:
                ax.text(x, y, str(int(c)), ha='center', va='center',
                    color='black')
    ax.legend(ncol=len(category_names), fontsize='medium')

    plt.savefig("Images/Charts/"+str(str(text)+"_HorizontalBarOverview"))
    # plt.show()

def ScatViewsLikes(data,text):
    # data=(Views, Likes, Exceptions) tuple of lists
    y = data[0] #Views
    x = data[1] #Likes
    Exceptions=data[2] #Footernotes
    available,unavailable,zeroboth,zeroviews,zerolikes=Exceptions[0],Exceptions[1],Exceptions[2],Exceptions[3],Exceptions[4]
    plt.figure(figsize=(10, 5))
    header="Views vs Likes in top search results \n"
    plt.title(header)
    plt.xlabel("Number of Likes")
    plt.ylabel("Number of Views")
    footer=str(available)+" Videos searched , Data unavailable for "+str(unavailable)+" videos"
    footer=footer+"\n Videos with views and likes both zero : "+str(zeroboth)+", Videos with only likes zero : "+str(zerolikes)+", Videos with only views zero : "+str(zeroviews)
    plt.figtext(0.51,-0.05,footer,ha="center",bbox={"facecolor":"red", "alpha":0.5, "pad":5})
    plt.scatter(x, y, marker='.', color='red')
    plt.savefig("Images/Charts/"+str(str(text)+"_ScatViewsLikes"),bbox_inches = 'tight')
    # plt.show()

def ScatLikesDislikes(data,text):
    # data=(Likes, Dislikes, Exceptions) tuple of lists
    y = data[0] #Likes
    x = data[1] #Dislikes
    Exceptions=data[2] #Footernotes
    available,unavailable,zeroboth,zerodislikes,zerolikes=Exceptions[0],Exceptions[1],Exceptions[2],Exceptions[3],Exceptions[4]
    plt.figure(figsize=(10, 5))
    plt.xlabel("Number of Dislikes")
    plt.ylabel("Number of Likes")
    header="Likes vs Dislikes in top search results \n"
    plt.title(header)
    footer=str(available)+" Videos searched , Data unavailable for "+str(unavailable)+" videos"
    footer=footer+"\n Videos with likes and dislikes both zero : "+str(zeroboth)+", Videos with only likes zero : "+str(zerolikes)+", Videos with only dislikes zero : "+str(zerodislikes)
    plt.figtext(0.51,-0.05,footer,ha="center",bbox={"facecolor":"red", "alpha":0.5, "pad":5})
    plt.scatter(x, y, marker='.', color='red')
    plt.savefig("Images/Charts/"+str(str(text)+"_ScatLikesDislikes"),bbox_inches = 'tight')
    # plt.show()

def ScatViewsComments(data,text):
    # data=(Views, Comments, Exceptions) tuple of lists
    y = data[0] #Views
    x = data[1] #Comments
    Exceptions=data[2] #Footernotes
    available,unavailable,zeroboth,zeroviews,zerocomments=Exceptions[0],Exceptions[1],Exceptions[2],Exceptions[3],Exceptions[4]
    plt.figure(figsize=(10, 5))
    header="Views vs Comments in top search results \n"
    plt.title(header)
    plt.xlabel("Number of Comments")
    plt.ylabel("Number of Views")
    footer=str(available)+" Videos searched , Data unavailable for "+str(unavailable)+" videos"
    footer=footer+"\n Videos with views and comments both zero : "+str(zeroboth)+", Videos with only comments zero : "+str(zerocomments)+", Videos with only views zero : "+str(zeroviews)
    plt.figtext(0.51,-0.05,footer,ha="center",bbox={"facecolor":"red", "alpha":0.5, "pad":5})
    plt.scatter(x, y, marker='.', color='red')
    plt.savefig("Images/Charts/"+str(str(text)+"_ScatViewsComments"),bbox_inches = 'tight')
    # plt.show()

def HorizontalBarAll4(data,text):
    newfont = 'Nirmala.ttf'

    # configure the Hindi font
    hindi_font = FontProperties(fname=newfont)
    category_colors=['lightblue','#00ff00','#ff4d4d', 'yellow']
    # create the dataframe
    df = pd.DataFrame(data, index=['Views', 'Likes', 'Dislikes', 'Comments'])
    # plot df
    ax = df.T.plot.barh(stacked=True, figsize=(30, 50), color=category_colors)
    ax.invert_yaxis()
    # get the y tick labels
    yticklab = [item.get_text() for item in ax.get_yticklabels()]

    # set the labels with the ttf
    ax.set_yticklabels(yticklab, fontproperties=hindi_font)
    header="Overall engagement of videos in top search results \n"
    plt.title(header,x=0.3,y=1, ha='center')
    # annotate the bars
    for rect in ax.patches:
        # Find where everything is located
        height = rect.get_height()
        width = rect.get_width()
        x = rect.get_x()
        y = rect.get_y()

        # The width of the bar is the count value and can used as the label
        label_text = int(round(10**width))

        label_x = x + width / 2
        label_y = y + height / 2

        # don't include label if it's equivalently 0
        if width > 0.001:
            ax.text(label_x, label_y, label_text, ha='center', va='center', fontsize=8)

    plt.savefig("Images/Charts/"+str(str(text)+"_HorizontalBarAll4"),bbox_inches = 'tight')
    # plt.show()

def TableChannels(ChannelCount,ChannelTopics, ChannelCategories,text):

    cells=[['','',''],['','',''],['','',''],['','',''],['','','']]


    count=0
    j=0
    for i in ChannelCount:
        if(count==5):
            break
        if ChannelCount[i]>1:
            cells[j][0]=i
            count+=1
            j=j+1


    count=0
    j=0
    for i in ChannelTopics:
        if(count==5):
            break

        cells[j][1]=i
        count+=1
        j=j+1

    count=0
    j=0
    for i in ChannelCategories:
        if(count==5):
            break
        cells[j][2]=i
        count+=1
        j=j+1


        
    columns = ("Most Popular Channels(>1 Videos)","Channel Topics", "Channel Categories")
    
    fig, ax = plt.subplots(figsize=(20, 7))
    ax.axis('tight')
    ax.axis('off')
    colors = [["#ffe6e6","#ffe6e6","#ffe6e6"],[ "#ff8080","#ff8080","#ff8080"],["#ffe6e6","#ffe6e6","#ffe6e6"],[ "#ff8080","#ff8080","#ff8080"],["#ffe6e6","#ffe6e6","#ffe6e6"]]
    colorshead = ["#1a0000","#1a0000","#1a0000"]

    the_table = ax.table(cellText=cells,colColours=colorshead,cellColours=colors,
                        colLabels=columns,loc='center')
    
    for i in range(3):
        the_table[(0, i)].get_text().set_color('white')
    the_table.scale(1, 4)
    header="Top channels, categories and topics from channels in top search results "
    plt.title(header,x=0.5,y=.95, ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_TableChannel"))
    # plt.show()


def TableVideos( VideoTags, VideoTopics, VideoCategories,text):
    negatives=['Unavailable','is','am','the','of','and','be',"in","for","that","these","bi"]
    cells=[['','',''],['','',''],['','',''],['','',''],['','','']]

    count=0
    j=0
    for i in VideoTags:
        if(count==5):
            break
        if (i not in negatives):
            cells[j][0]=i
            count+=1
            j=j+1

    count=0
    j=0
    for i in VideoTopics:
        if(count==5):
            break
        if (i not in negatives):
            cells[j][1]=i
            count+=1
            j=j+1

    count=0
    j=0
    for i in VideoCategories:
        if(count==5):
            break
        if (i not in negatives):
            cells[j][2]=i
            count+=1
            j=j+1

        
    columns = ("Video Tags", "Video Topics", "Video Categories")
    
    fig, ax = plt.subplots(figsize=(20, 7))
    ax.axis('tight')
    ax.axis('off')
    colors = [["#ffe6e6","#ffe6e6","#ffe6e6"],[ "#ff8080","#ff8080","#ff8080"],["#ffe6e6","#ffe6e6","#ffe6e6"],[ "#ff8080","#ff8080","#ff8080"],["#ffe6e6","#ffe6e6","#ffe6e6"]]
    colorshead = ["#1a0000","#1a0000","#1a0000"]

    the_table = ax.table(cellText=cells,colColours=colorshead,cellColours=colors,
                        colLabels=columns,loc='center')
    
    for i in range(3):
        the_table[(0, i)].get_text().set_color('white')
    the_table.scale(1, 4)
    header="Top topics, categories and tags from videos in top search results "
    plt.title(header,x=0.5,y=.95, ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_TableVideos"))
    # plt.show()