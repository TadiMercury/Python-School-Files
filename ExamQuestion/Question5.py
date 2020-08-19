CDTitle = ''
CDArstist = ''
CDLocation = ''
TextLine = ''

#def InputData (CDTitle,CDArstist,CDLocation,TextLine):
CDTitle = input("Input CD Title: ")
CDArstist = input("Input CD Artist: ")
CDLocation = input("Input CD Location: ")
TextLine = CDTitle + CDArstist + CDLocation

file_path = "SongFile.txt"
file = open(file_path,"w")
file.write(TextLine)
file.close()
print(TextLine)
    
