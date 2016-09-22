from os import path, mkdir

settings = {}
execfile("settings.py", settings)


def makeFile(FileName):
    if not path.exists(FileName):
        mkdir(FileName)


makeFile(settings["files_directory_name"])
makeFile(settings["matrix_directory_name"])

execfile("getFollowersList.py")
execfile("getFollowingList.py")
execfile("generateEdgesMatrix.py")
