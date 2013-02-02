import BookHandler

if __name__ == "__main__":
    myBookHandler = BookHandler.BookHandler()
    myBook = myBookHandler.getBookById("abb")
    print myBook.getRating()



