#A book handler 
import urllib2
import json

class Book:
    '''
    Data structure of a book
    '''
    def __init__(self, jsonStr):   
        '''
        Book Constructor. Build a book data structure with json.

        json -- book info in json format
        '''
        self.jData = json.loads(jsonStr)

    def getRating(self):
        '''
        Get rating, return dictionary
        {"max": 10, "numRaters":270, "average":"9.0", "min":0}
        '''
        return self.jData['rating']

    def getSubtitle(self):
        '''Get subtitle'''
        return self.jData['subtitle']


    def getPubdate(self):
        '''Get publish date'''
        return self.jData['pubdate']

    def getImageUrl(self):
        '''Get image url'''
        return self.jData['image']

    def getBinding(self):
        '''Get binding'''
        return self.jData['binding']

    def getTitle(self):
        '''get title'''
        return self.jData['title']

#    def get







class BookHandler:              #TODO: Create response codes, catch exceptions
    '''
    A book handler to get book
    '''
    def __init__(self):
        self.responses = {          #Response code table
                404: ('Book_not_found')
                }



    def getBookById(self, bookId):
        '''
        Get book by its id on douban
        bookId -- book id
        '''
        f = file("book.json","r")
        json = f.read()
        book = Book(json)
        return book
        



        


    def getBookByISBN(self, isbn):
        '''
        get book by its isbn
        isbn -- ISBN
        '''
        pass

    def searchBookByName(self, name):
        '''
        Search book by name
        name -- book name or key words to search
        '''
        pass

    

