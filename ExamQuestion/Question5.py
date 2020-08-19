CDTitle = ''
CDArstist = ''
CDLocation = ''

def InputData (CDTitle,CDArstist,CDLocation,TextLine):
    CDTitle = input("Input CD Title: ")
    CDArstist = input("Input CD Artist: ")
    CDLocation = input("Input CD Location: ")

    TextLine = CDTitle + CDArstist + CDLocation
    
