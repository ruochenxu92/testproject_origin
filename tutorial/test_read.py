__author__ = 'Xiaomin'
import os
'''
get list of professors
'''
def getListOfProfessors():
    path = os.path.abspath("/Users/Xiaomin/testproject/tutorial/professor.txt")
    f = open(path)
    listOfProfessors = f.read().split('\n')
    return listOfProfessors


 # self.file = open('items.json', 'wb')
 #        self.file.write('[')
def getStartUrls():
    prefix = 'https://scholar.google.com/scholar?q='
    suffix = '&btnG=&hl=en&as_sdt=0%2C14'
    start_urls = []
    listOfProfessors = getListOfProfessors()
    for prof in listOfProfessors:
        start_urls.append(prefix + prof + suffix)
    return start_urls

print(getStartUrls())