def getFolder():
    """ return the folder where this module is located"""
    folderWithFileName = __file__
    if folderWithFileName[-1] == 'c':
        fileName = __name__ + ".pyc"
    else:
        fileName = __name__ + ".py"
    folderLength = len(folderWithFileName) - len(fileName)
    folderWithoutFileName = folderWithFileName[:folderLength]

    return folderWithoutFileName
