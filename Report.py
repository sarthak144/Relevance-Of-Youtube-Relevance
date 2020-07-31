from reportlab.pdfgen import canvas 
from reportlab.platypus import Paragraph, Frame
# from reportlab import platypus
# from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
# from reportlab.lib import colors
from math import sqrt
from math import ceil



def GetReport(text,NumPages,NumChannel,NumVideo,region,start_time):

    # ------------------------------------------------------------------------
    BarChannelAge="Images/"+str(text)+"/Charts/"+str(str(text)+"_BarChannelAge")+".png"
    BarChannelViews="Images/"+str(text)+"/Charts/"+str(str(text)+"_BarChannelViews")+".png"
    BarChannelSubscribers="Images/"+str(text)+"/Charts/"+str(str(text)+"_BarChannelSubscribers")+".png"
    BarChannelVideos="Images/"+str(text)+"/Charts/"+str(str(text)+"_BarChannelVideos")+".png"
    BarVideoAges="Images/"+str(text)+"/Charts/"+str(str(text)+"_BarVideoAges")+".png"
    BarVideoDuration="Images/"+str(text)+"/Charts/"+str(str(text)+"_BarVideoDuration")+".png"
    BarVideoViews="Images/"+str(text)+"/Charts/"+str(str(text)+"_BarVideoViews")+".png"
    ScatViewsLikes="Images/"+str(text)+"/Charts/"+str(str(text)+"_ScatViewsLikes")+".png"
    ScatLikesDislikes="Images/"+str(text)+"/Charts/"+str(str(text)+"_ScatLikesDislikes")+".png"
    ScatViewsComments="Images/"+str(text)+"/Charts/"+str(str(text)+"_ScatViewsComments")+".png"
    HorizontalBarOverview="Images/"+str(text)+"/Charts/"+str(str(text)+"_HorizontalBarOverview")+".png"
    HorizontalBarAll4="Images/"+str(text)+"/Charts/"+str(str(text)+"_HorizontalBarAll4")+".png"
    TableChannel="Images/"+str(text)+"/Charts/"+str(str(text)+"_TableChannel")+".png"
    TableVideos="Images/"+str(text)+"/Charts/"+str(str(text)+"_TableVideos")+".png"
    TableThumbnail="Images/"+str(text)+"/Charts/"+str(str(text)+"_TableThumbnails")+".png"



    # ------------------------------------------------------------------------


    fileName = 'Analystics-RoYR-'+str(text)+'.pdf'
    documentTitle = 'Analystics-RoYR-'+str(text)
    title = 'Relevance of Youtube Relevance'
    subtitle="Analysis of a random youtube search from a non personalized account."
    pdfmetrics.registerFont(TTFont('OurFont', 'Nirmala.ttf'))
    pdf = canvas.Canvas(fileName)

    # print(pdf.getAvailableFonts())
    pdf.setTitle(documentTitle)
    # drawMyRuler(pdf)
    def drawMyRuler(pdf):
        pdf.setFont('Helvetica', 4)
        pdf.drawString(0,830, str((0,830)))
        x=50
        while(x<=550):
            pdf.drawString(x,830, str((x,830)))
            x+=50
        pdf.drawString(575,830, str((575,830)))
        pdf.drawString(0,10, str((0,10)))
        y=50
        while(y<=800):
            pdf.drawString(0,y, str((0,y)))
            y=y+50  

    def TitleText():
        pdf.setFillColorRGB(255, 0, 0)
        pdf.setFont('Helvetica-Bold',8)

    def ResultText():
        pdf.setFillColorRGB(0, 0, 0)
        pdf.setFont('Helvetica',8)

    def HeaderText1():
        pdf.setFillColorRGB(0, 0, 0)
        pdf.setFont('Helvetica-Bold',12)

    def HeaderText2():
        pdf.setFillColorRGB(0, 0, 0)
        pdf.setFont('Helvetica-Bold',10)
    # ------------------------------------------------------------------------
    pdf.setFont('Helvetica-Bold',24)
    pdf.drawCentredString(290, 790, title)
    HeaderText2()
    pdf.drawCentredString(290, 770, subtitle)
    subtitle="By Sarthak Arora"
    pdf.drawCentredString(290, 755, subtitle)

    items = []
    link = '<link href = "mailto:sarthak18307@iiitd.ac.in">Send Email</link>'
    items.append(Paragraph(link))
    f = Frame(200, 730, 70, 25, showBoundary=0)
    f.addFromList(items, pdf)

    items = []
    link = '<link href="https://github.com/sarthak144">Github</link>'
    items.append(Paragraph(link))
    f = Frame(270, 730, 50, 25, showBoundary=0)
    f.addFromList(items, pdf)

    items = []
    link = '<link href="https://www.linkedin.com/in/sarthak-arora-82100b17b/">LinkedIn</link>'
    items.append(Paragraph(link))
    f = Frame(320, 730, 50, 25, showBoundary=0)
    f.addFromList(items, pdf)
    # ------------------------------------------------------------------------

        
    xoverview=50
    yoverview=700
    pdf.line(50, yoverview+20, 530, yoverview+20)
    TitleText()
    pdf.drawString(xoverview, yoverview, "String Searched")
    ResultText()
    pdf.drawString(xoverview+80, yoverview, ":  "+str(text))
    TitleText()
    pdf.drawString(xoverview, yoverview-10, "Pages Searched")
    ResultText()
    pdf.drawString(xoverview+80, yoverview-10, ":  "+str(NumPages))
    TitleText()
    pdf.drawString(xoverview, yoverview-20, "Channels Searched")
    ResultText()
    pdf.drawString(xoverview+80, yoverview-20, ":  "+str(NumChannel))
    TitleText()
    pdf.drawString(xoverview, yoverview-30, "Videos Searched")
    ResultText()
    pdf.drawString(xoverview+80, yoverview-30, ":  "+str(NumVideo))
    TitleText()
    pdf.drawString(xoverview, yoverview-40, "Country Origin")
    ResultText()
    pdf.drawString(xoverview+80, yoverview-40, ":  "+str(region))
    TitleText()
    pdf.drawString(xoverview, yoverview-50, "Date and Time")
    ResultText()
    pdf.drawString(xoverview+80, yoverview-50, ":  "+str(start_time))
    pdf.line(50, yoverview-70, 530, yoverview-70)


    # ------------------------------------------------------------------------

    ytables=yoverview-100
    HeaderText2()
    header="Top channels, categories and topics from channels in top search results"
    pdf.drawInlineImage(TableChannel, 10, ytables-190, height=200,width=200*2.77)
    pdf.drawCentredString(290, ytables, header)



    ytables=ytables-190

    header="Top topics, categories and tags from videos in top search results"
    pdf.drawInlineImage(TableVideos, 10, ytables-190, height=200,width=200*2.77)
    pdf.drawCentredString(290, ytables, header)

    ytables=ytables-190
    header="Various aspects of top search results"
    pdf.drawInlineImage(HorizontalBarOverview, 50, ytables-165, height=150,width=150*3.2)
    pdf.drawCentredString(290, ytables, header)

    pdf.showPage()

    # ------------------------------------------------------------------------
    HeaderText2()
    ybar=800
    xbar1=7
    xbar2=xbar1+300
    header1="Age of channels in top search results"
    header2="Video count of channels in top search results"
    pdf.drawInlineImage(BarChannelAge, xbar1, ybar-160, height=140,width=280)
    pdf.drawInlineImage(BarChannelVideos, xbar2, ybar-160, height=140,width=280)
    pdf.drawCentredString(xbar1+150, ybar, header1)
    pdf.drawCentredString(xbar2+150, ybar, header2)

    ybar=ybar-200

    header1="Subscriber count of channels in top search results"
    header2="View count of channels in top search results"
    pdf.drawInlineImage(BarChannelSubscribers, xbar1, ybar-160, height=140,width=280)
    pdf.drawInlineImage(BarChannelViews, xbar2, ybar-160, height=140,width=280)
    pdf.drawCentredString(xbar1+150, ybar, header1)
    pdf.drawCentredString(xbar2+150, ybar, header2)

    ybar=ybar-200

    header1="Views of videos in top search results"
    header2="Age of videos in top search results"
    pdf.drawInlineImage(BarVideoViews, xbar1, ybar-160, height=140,width=280)
    pdf.drawInlineImage(BarVideoAges, xbar2, ybar-160, height=140,width=280)
    pdf.drawCentredString(xbar1+150, ybar, header1)
    pdf.drawCentredString(xbar2+150, ybar, header2)

    ybar=ybar-200
    header1="Length of videos in top search results"
    pdf.drawInlineImage(BarVideoDuration, xbar1+150, ybar-160, height=140,width=280)
    pdf.drawCentredString(xbar1+300, ybar, header1)

    pdf.showPage()
    # ------------------------------------------------------------------------
    HeaderText2()
    yscatter=800
    xscatter=15
    header1="Views vs Likes in top search results"
    pdf.drawInlineImage(ScatViewsLikes, xscatter+80, yscatter-230, height=220,width=220*1.73)
    pdf.drawCentredString(xscatter+275, yscatter, header1)

    header1="Likes vs Dislikes in top search results"
    yscatter=yscatter-270
    pdf.drawInlineImage(ScatLikesDislikes, xscatter+80, yscatter-230, height=220,width=220*1.73)
    pdf.drawCentredString(xscatter+275, yscatter, header1)

    header1="Views vs Comments in top search results"
    yscatter=yscatter-270
    pdf.drawInlineImage(ScatViewsComments, xscatter+80, yscatter-230, height=220,width=220*1.73)
    pdf.drawCentredString(xscatter+275, yscatter, header1)

    pdf.showPage()
    # ------------------------------------------------------------------------
    HeaderText1()
    yall=800
    xall=50
    header1="Detailed engagement of videos in top search results"
    pdf.drawInlineImage(HorizontalBarAll4, xall, yall-670, height=500*1.27,width=500)
    pdf.drawCentredString(xall+240, yall, header1)
    # drawMyRuler(pdf)
    pdf.showPage()
    # ------------------------------------------------------------------------


    HeaderText1()
    header1="Analysis of thumbnails of videos in top search results"
    pdf.drawCentredString(290, 800, header1)

    NumberImages=NumVideo
    factor=((sqrt(NumberImages/12)))
    NumRows=int(ceil(3*factor))
    NumColumns=int(ceil(4*factor))
    # print(NumRows, NumColumns)
    ImageWidth=480/NumColumns
    ImageHeight=360/NumRows
    y=770
    x=60
    count=1
    for i in range(NumRows):
        if count>NumberImages:
            break
        y=y-ImageHeight
        x=60
        for j in range(NumColumns):
            if count>NumberImages:
                break
            try:
                pdf.drawInlineImage("Images/"+str(text)+"/Thumbnails/"+str(count)+".jpg", x, y, height=ImageHeight,width=ImageWidth)
                count+=1
                x=x+ImageWidth
            except:
                print(str(count)+".jpg not available to put in collage")


    y=370
    header="Top subjects present in thumbnails of videos in top search results"
    pdf.drawInlineImage(TableThumbnail, 10, y-190, height=200,width=200*2.77)
    pdf.drawCentredString(300, y, header)



    pdf.save()