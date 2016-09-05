from os import path, mkdir

settings = {}
execfile("settings.py", settings)


def makeFile(FileName = settings["directory_name"]):
    if not path.exists(FileName):
        mkdir(FileName)


makeFile()

execfile("getFollowersList.py")
execfile("getFollowingList.py")
