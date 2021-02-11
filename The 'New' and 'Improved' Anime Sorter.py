import os
import shutil
import time

Source_Path = "H:/Anime/Airing/"
Destination_Path = "H:/Anime/Auto Synced/"

Filenames = os.listdir(Source_Path)

def UserExtractor(Filename):
    Username = Filename[Filename.find("[") + 1:Filename.find("]")]
    return (Username)

def TitleExtractor(Filename):
    ReverseName = Filename[::-1]
    Title = ""
    if Filename.find(" - ") != -1:
        Title = Filename[Filename.find("]")+2:(len(Filename) - ReverseName.find(" - ")) - 3]
    elif Filename.find(" [") != -1:
        Filename = Filename[Filename.find("]")+2:]
        Title = Filename[:Filename.find("[")-1]
    elif Filename.find(" (") != -1:
        Filename = Filename[Filename.find("]")+2:]
        Title = Filename[:Filename.find("(")-1]
    return (Title)

def QualityExtractor(Filename):
    Quality = ""
    if Filename.find("1080") != -1 or Filename.find("1980") != -1:
        Quality = "1080p"
    if Filename.find("720") != -1 or Filename.find("1280") != -1:
        Quality = "720p"
    if Filename.find("480") != -1:
        Quality = "480p"
    if Filename.find("540") != -1:
        Quality = "540p"
    if Filename.find("360") != -1:
        Quality = "360p"
    return (Quality)

def CheckerMover(Filename):
    UserDirectory = os.path.join(Destination_Path, UserExtractor(Filename))
    if not os.path.exists(UserDirectory):
        os.mkdir(UserDirectory)
    TitleDirectory = os.path.join(Destination_Path, UserExtractor(Filename), TitleExtractor(Filename))
    if not os.path.exists(TitleDirectory):
        os.mkdir(TitleDirectory)
    QualityDirectory = os.path.join(Destination_Path, UserExtractor(Filename), TitleExtractor(Filename), QualityExtractor(Filename))
    if not os.path.exists(QualityDirectory):
        os.mkdir(QualityDirectory)
    shutil.move(Source_Path + Filename, QualityDirectory)

StartTime = time.time()

for i in range(len(Filenames)):
    print ("Moving " + Filenames[i] + " right now... ")
    CheckerMover(Filenames[i])
    print (i + 1, " of ", len(Filenames), " done!")

EndTime = time.time()
print("Finished sorting in: ", EndTime - StartTime)
 



    
                                                
                
                
                
                
