import os
import shutil

Source_Path = "B:/Anime/Airing/"
Destination_Path = "B:/Anime/Auto Synced/"

Filenames = os.listdir(Source_Path)

def UserExtractor(Filename):
    Username = Filename[Filename.find("[") + 1:Filename.find("]")]
    return (Username)

def TitleExtractor(Filename):
    ReverseName = Filename[::-1]
    Title = "rectification_required"
    if ReverseName.find(" - ") != -1:
        Title = ""
        Title = Filename[Filename.find("]")+2:(len(Filename) - ReverseName.find(" - ")) - 3]
    return (Title)

def QualityExtractor(Filename):
    Quality = "rectification_required"
    if Filename.find("1080") != -1 or Filename.find("1980") != -1:
        Quality = "1080p"
    if Filename.find("720") != -1 or Filename.find("1280") != -1:
        Quality = "720p"
    if Filename.find("480") != -1:
        Quality = "480p"
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

for i in Filenames:
    CheckerMover(i)

 



    
                                                
                
                
                
                
