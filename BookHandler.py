import urllib
import urllib2
import json

class BookHandler:
    '''
    Get book data
    '''
    def __init__(self):
        #TODO Initialize the handler
        #f = open('books.json', 'r')
        self.url = 'https://api.douban.com/v2/book/search'
        self.key = {}
        
    def search(self, keyword):
        #Search info by keyword
        
        result = []
        '''
        self.key['q'] = keyword
        data = urllib.urlencode(self.key)
        req =  urllib2.Request(self.url, data)
        response = urllib2.urlopen(req)
        page = response.read()
        '''
        page = open('books.json', 'r').read()
        jData = json.loads(page)
        for book in jData['books']:
            result.append(Book(book))
        return result

class Book:
    '''
    Book data structure
    '''
    def __init__(self, jData):
        #TODO Initialize book data with a json file
        self.jData = jData
    def getSubtitle(self):
        return self.jData['subtitle']
    def getTitle(self):
        return self.jData['title']
    def getPubdate(self):
        return self.jData['pubdate']
    def getImage(self):
        return self.jData['image']
    def getRating(self):
        return self.jData['rating']['average']
    def getPages(self):
        return self.jData['pages']
    def getPublisher(self):
        return self.jData['publisher']
    def getISBN10(self):
        return self.jData['isbn10']
    def getAuthor(self):
        return self.jData['author']
    def getSummary(self):
        return self.jData['summary']
        


