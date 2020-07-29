import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def BarChannelAge(data,text):
    xtags = list(data.keys()) 
    yvalues = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(xtags, yvalues, color ='#ff4d4d',  width = 0.4)
    plt.xlabel("Age of channels")
    plt.ylabel("Number of channels")
    # plt.title("Age of channels in top search results")
    for x,y in zip(xtags,yvalues):
        label = format(y)
        plt.annotate(label, # Lable on top of the bar
                    (x,y), # the coordinated of label
                    textcoords="offset points", # how to position the text
                    xytext=(0,3), # distance from text to points (x,y)
                    ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_BarChannelAge")+".png",bbox_inches = 'tight')
    # plt.show()

def BarChannelViews(data,text):
    xtags = list(data.keys()) 
    yvalues = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(xtags, yvalues, color ='#ff4d4d',  width = 0.4)
    plt.xlabel("Views of channels")
    plt.ylabel("Number of channels")
    # plt.title("View count of channels in top search results")
    for x,y in zip(xtags,yvalues):
        label = format(y)
        plt.annotate(label, # Lable on top of the bar
                    (x,y), # the coordinated of label
                    textcoords="offset points", # how to position the text
                    xytext=(0,3), # distance from text to points (x,y)
                    ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_BarChannelViews")+".png",bbox_inches = 'tight')
    # plt.show()

def BarChannelSubscribers(data,text):
    xtags = list(data.keys()) 
    yvalues = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(xtags, yvalues, color ='#ff4d4d',  width = 0.4)
    plt.xlabel("Number of subscribers of channels")
    plt.ylabel("Number of channels")
    # plt.title("Subscriber count of channels in top search results")
    for x,y in zip(xtags,yvalues):
        label = format(y)
        plt.annotate(label, # Lable on top of the bar
                    (x,y), # the coordinated of label
                    textcoords="offset points", # how to position the text
                    xytext=(0,3), # distance from text to points (x,y)
                    ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_BarChannelSubscribers")+".png",bbox_inches = 'tight')
    # plt.show()

def BarChannelVideos(data,text):
    xtags = list(data.keys()) 
    yvalues = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(xtags, yvalues, color ='#ff4d4d',  width = 0.4)
    plt.xlabel("Number of videos of channels")
    plt.ylabel("Number of channels")
    # plt.title("Video count of channels in top search results")
    for x,y in zip(xtags,yvalues):
        label = format(y)
        plt.annotate(label, # Lable on top of the bar
                    (x,y), # the coordinated of label
                    textcoords="offset points", # how to position the text
                    xytext=(0,3), # distance from text to points (x,y)
                    ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_BarChannelVideos")+".png",bbox_inches = 'tight')
    # plt.show()

def BarVideoAges(data,text):
    xtags = list(data.keys()) 
    yvalues = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(xtags, yvalues, color ='#ff4d4d',  width = 0.4)
    plt.xlabel("Age of videos")
    plt.ylabel("Number of videos")
    # plt.title("Age of videos in top search results")
    for x,y in zip(xtags,yvalues):
        label = format(y)
        plt.annotate(label, # Lable on top of the bar
                    (x,y), # the coordinated of label
                    textcoords="offset points", # how to position the text
                    xytext=(0,3), # distance from text to points (x,y)
                    ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_BarVideoAges")+".png",bbox_inches = 'tight')
    # plt.show()

def BarVideoDuration(data,text):
    xtags = list(data.keys()) 
    yvalues = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(xtags, yvalues, color ='#ff4d4d',  width = 0.4)
    plt.xlabel("Length of videos")
    plt.ylabel("Number of videos")
    # plt.title("Length of videos in top search results")
    for x,y in zip(xtags,yvalues):
        label = format(y)
        plt.annotate(label, # Lable on top of the bar
                    (x,y), # the coordinated of label
                    textcoords="offset points", # how to position the text
                    xytext=(0,3), # distance from text to points (x,y)
                    ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_BarVideoDuration")+".png",bbox_inches = 'tight')
    # plt.show()

def BarVideoViews(data,text):
    xtags = list(data.keys()) 
    yvalues = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(xtags, yvalues, color ='#ff4d4d',  width = 0.4)
    plt.xlabel("Views of videos")
    plt.ylabel("Number of videos")
    # plt.title("Views of videos in top search results")
    for x,y in zip(xtags,yvalues):
        label = format(y)
        plt.annotate(label, # Lable on top of the bar
                    (x,y), # the coordinated of label
                    textcoords="offset points", # how to position the text
                    xytext=(0,3), # distance from text to points (x,y)
                    ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_BarVideoViews")+".png",bbox_inches = 'tight')
    # plt.show()



def ScatViewsLikes(data,text):
    # data=(Views, Likes, Exceptions) tuple of lists
    y = data[0] #Views
    x = data[1] #Likes
    Exceptions=data[2] #Footernotes
    available,unavailable,zeroboth,zeroviews,zerolikes=Exceptions[0],Exceptions[1],Exceptions[2],Exceptions[3],Exceptions[4]
    plt.figure(figsize=(10, 5))
    header="Views vs Likes in top search results \n"
    # plt.title(header)
    plt.xlabel("Number of Likes")
    plt.ylabel("Number of Views")
    footer=str(available)+" Videos searched , Data unavailable for "+str(unavailable)+" videos"
    footer=footer+"\n Videos with views and likes both zero : "+str(zeroboth)+", Videos with only likes zero : "+str(zerolikes)+", Videos with only views zero : "+str(zeroviews)
    plt.figtext(0.51,-0.05,footer,ha="center",bbox={"facecolor":"red", "alpha":0.5, "pad":5})
    plt.scatter(x, y, marker='.', color='red')
    plt.savefig("Images/Charts/"+str(str(text)+"_ScatViewsLikes")+".png",bbox_inches = 'tight')
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
    # plt.title(header)
    footer=str(available)+" Videos searched , Data unavailable for "+str(unavailable)+" videos"
    footer=footer+"\n Videos with likes and dislikes both zero : "+str(zeroboth)+", Videos with only likes zero : "+str(zerolikes)+", Videos with only dislikes zero : "+str(zerodislikes)
    plt.figtext(0.51,-0.05,footer,ha="center",bbox={"facecolor":"red", "alpha":0.5, "pad":5})
    plt.scatter(x, y, marker='.', color='red')
    plt.savefig("Images/Charts/"+str(str(text)+"_ScatLikesDislikes")+".png",bbox_inches = 'tight')
    # plt.show()

def ScatViewsComments(data,text):
    # data=(Views, Comments, Exceptions) tuple of lists
    y = data[0] #Views
    x = data[1] #Comments
    Exceptions=data[2] #Footernotes
    available,unavailable,zeroboth,zeroviews,zerocomments=Exceptions[0],Exceptions[1],Exceptions[2],Exceptions[3],Exceptions[4]
    plt.figure(figsize=(10, 5))
    plt.xlabel("Number of Comments")
    plt.ylabel("Number of Views")
    header="Views vs Comments in top search results \n"
    # plt.title(header)
    footer=str(available)+" Videos searched , Data unavailable for "+str(unavailable)+" videos"
    footer=footer+"\n Videos with views and comments both zero : "+str(zeroboth)+", Videos with only comments zero : "+str(zerocomments)+", Videos with only views zero : "+str(zeroviews)
    plt.figtext(0.51,-0.05,footer,ha="center",bbox={"facecolor":"red", "alpha":0.5, "pad":5})
    plt.scatter(x, y, marker='.', color='red')
    plt.savefig("Images/Charts/"+str(str(text)+"_ScatViewsComments")+".png",bbox_inches = 'tight')
    # plt.show()



def HorizontalBarOverview(data,text):
    newfont = 'Nirmala.ttf'

    # configure the Hindi font
    hindi_font = FontProperties(fname=newfont)
    category_colors=['#00ff00','#ff4d4d','lightgrey']
    # create the dataframe
    df = pd.DataFrame(data, index=['Yes', 'No', 'Unavailable'])
    # plot df
    ax = df.T.plot.barh(stacked=True, figsize=(15, 5), color=category_colors)
    ax.invert_yaxis()
    # get the y tick labels
    yticklab = [item.get_text() for item in ax.get_yticklabels()]

    # set the labels with the ttf
    ax.set_yticklabels(yticklab, fontproperties=hindi_font)
    header="Various aspects of top search results \n"
    # plt.title(header,x=0.3,y=1, ha='center')
    # annotate the bars
    for rect in ax.patches:
        # Find where everything is located
        height = rect.get_height()
        width = rect.get_width()
        x = rect.get_x()
        y = rect.get_y()

        # The width of the bar is the count value and can used as the label
        label_text = int(width)

        label_x = x + width / 2
        label_y = y + height / 2

        # don't include label if it's equivalently 0
        if width > 0.001:
            ax.text(label_x, label_y, label_text, ha='center', va='center', fontsize=8)

    plt.savefig("Images/Charts/"+str(str(text)+"_HorizontalBarOverview")+".png",bbox_inches = 'tight')
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
    # plt.title(header,x=0.3,y=1, ha='center')
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

    plt.savefig("Images/Charts/"+str(str(text)+"_HorizontalBarAll4")+".png",bbox_inches = 'tight')
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
    # plt.title(header,x=0.5,y=.95, ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_TableChannel")+".png",bbox_inches = 'tight')
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
    # plt.title(header,x=0.5,y=.95, ha='center')
    plt.savefig("Images/Charts/"+str(str(text)+"_TableVideos")+".png",bbox_inches = 'tight')
    # plt.show()