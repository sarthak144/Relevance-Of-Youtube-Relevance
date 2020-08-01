# Relevance Of Youtube Relevance


## Table of Contents

- [Getting Started](#Getting-Started)
- [Aim](#Aim)
- [Resources Used](#Resources-Used)
    - [Language](#Language)
    - [Libraries (Gerneral)](#Libraries-(Gerneral))
    - [Libraries (Visualization)](#Libraries-(Visualization))
    - [Libraries (Data Retrieval)](#Libraries-(Data-Retrieval))
    - [Libraries (Reporting)](#Libraries-(Reporting))
    - [APIs](#-APIs)
- [Installing](#Installing)
- [Deployment](#Deployment)
- [Results](#Results)



## Getting Started
_Why is youtube showing this set of videos on searching XYZ?_ <br>
_Which channel's most videos make it to the top search results?_ <br>
_How relevant are youtube search results for me?_  <br><br>

Obviously none except people at youtube tell how youtube search algorithm works but if you ever have searched on youtube **anonymously**, you might have noticed that by default the seach filter is set to **Relevance**. This project aims to analyse the top search results which a user may get upon searching anything on Youtube.com from a **non-personalized account**.

## Aim 
Considering that youtube algorithms work different for different people. (Sorry Kant!) We will analyse the top search results that are selected from millions of videos on youtube. All the search results retrieved would be formatted and then respresented so as to get better understanding of the trends.

## Resources Used

### Language
- Python 3.7

### Libraries (Gerneral)
- dateutil
- datetime
- math

### Libraries (Visualization)
- numpy
- pandas
- matplotlib

### Libraries (Data Retrieval)
- apiclient
- urllib
- clarifai

### Libraries (Reporting)
- reportlab

### APIs
- Youtube Data API v3
- Clarifai General Visual Recogonition
- IBM Watson (Used in Initial Versions)




## Installing

You can install each library from pypi.org 
In some cases where you get imaging related problems, try installing pillow.

```
pip install Pillow-PIL
```

You can get Youtube Data API key from [Google Cloud](https://console.cloud.google.com) and Clarifai API from [Clarifai](https://portal.clarifai.com/login)



## Deployment

After cloning the repo, add Youtube Data API key to ```Search.py``` file and Clarifai API key to ```ThumbnailAnalyser.py``` file. <br>

One can change the string they want to seach and the number of pages in ```Main.py``` file.
The default and the maximum number results per page is 50, this can be decreased in ```Search.py``` file.

After configuring all the requirements, run the ```Main.py``` file.

## Results

After running ```Main.py```, one can find ```Analystics-RoYR-<Searched String>.pdf``` in the main directory.<br>

![Report](https://user-images.githubusercontent.com/43843585/89098863-c8170480-d408-11ea-86a5-25288451bcdc.gif)

