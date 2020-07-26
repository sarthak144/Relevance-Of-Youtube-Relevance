import numpy as np
import matplotlib.pyplot as plt

def BarChannelAge(data, text):
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
    plt.savefig(str(str(text)+"_BarChannelAge"))
    # plt.show()

def BarChannelViews(data, text):
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
    plt.savefig(str(str(text)+"_BarChannelViews"))
    # plt.show()

def BarChannelSubscribers(data):
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
    plt.show()

def BarChannelVideos(data):
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
    plt.show()

def BarVideoAges(data):
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
    plt.show()

def BarVideoDuration(data):
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
    plt.show()

def BarVideoViews(data):
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
    plt.show()

def HorizontalBarOverview(data):
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

    category_colors=['#00ff00','red','lightgrey']

    fig, ax = plt.subplots(figsize=(10, 15))
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
    ax.legend(ncol=len(category_names))

    plt.show()

def ScatViewsLikes(data):
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
    plt.show()

def ScatLikesDislikes(data):
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
    plt.show()

def ScatViewsComments(data):
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
    plt.show()

def HorizontalBarAll4(data):
    category_names = ['Views', 'Likes', 'Dislikes', 'Comments']
    labels = list(data.keys())
    data = np.array(list(data.values()))
    data_cum = data.cumsum(axis=1)

    category_colors=['lightblue','#00ff00','#ff4d4d', 'yellow']

    fig, ax = plt.subplots(figsize=(30, 50))
    ax.invert_yaxis()
    ax.set_xlim(0, np.sum(data, axis=1).max())
    
    fontsup=FontProperties(fname = 'Nirmala.ttf')
    ax.set_yticklabels(labels, rotation=0, fontsize=10, fontproperties=fontsup)
    header="Overall engagement of videos in top search results \n"
    plt.title(header,x=0.3,y=1, ha='center')
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color )
        xcenters = starts + widths / 2
        
        for y, (x, c) in enumerate(zip(xcenters, widths)):
            if int(c)!=0:
                ax.text(x, y, str(int(round(10**c))), ha='center', va='center',
                    color='black', size="x-small")
    ax.legend(ncol=len(category_names))

    plt.show()