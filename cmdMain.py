import urwid
import BookHandler


class Menu:
    def __init__(self, books):
        self.books = books
        self.menu = []
        index = 0
        for book in self.books:
            itemString = str(index) + '. ' + book.getTitle()
            if book.getSubtitle() != '':
                itemString = itemString + ": " + book.getSubtitle()
            itemString = itemString + "\n"
            for author in book.getAuthor():
                itemString = itemString + author + '  '
            self.menu.append(itemString)
            index = index + 1

    def mainMenu(self):
        title = 'Main Menu'
        body = [urwid.Text(title), urwid.Divider()]
        for c in self.menu:
            button = urwid.Button(c)
            urwid.connect_signal(button, 'click', self.item_chosen, c.split('.')[0])        #Pass index to the chosen item
            body.append(urwid.AttrMap(button, None, focus_map='reversed'))
        exitButton = urwid.Button('*************************Exit*****************************')
        urwid.connect_signal(exitButton, 'click', self.exit_program)
        body.append(urwid.AttrMap(exitButton, None, focus_map='reversed'))
        return urwid.ListBox(urwid.SimpleFocusListWalker(body))

    def item_chosen(self, button, choice):
        chosenBook = self.books[int(choice)]
        title = chosenBook.getTitle()
        if chosenBook.getSubtitle() != '':
            title = title + ": " + chosenBook.getSubtitle()
        authors = ''
        for author in chosenBook.getAuthor():
            authors = authors + author + '    '
        publisher = chosenBook.getPublisher()
        pubdate = chosenBook.getPubdate()
        rating = chosenBook.getRating()
        summary = chosenBook.getSummary()
        response = urwid.Text(title+'\n'+authors+'\n'+publisher+'\n'+pubdate+'\n'+summary)
        done = urwid.Button(u'Ok')
        urwid.connect_signal(done, 'click', self.exit_program)
        self.main.original_widget = urwid.Filler(urwid.Pile([
            response, urwid.AttrMap(done, None, focus_map='reversed')]))

    def exit_program(self, button):
        raise urwid.ExitMainLoop()

    def exit_on_q(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
        if key in ('f', 'F'):
#TODO start a new search
            pass;


    def runLoop(self):
        self.main = urwid.Padding(self.mainMenu(), left=2, right=2)
        self.top = urwid.Overlay(self.main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
            align='center', width=('relative', 95),
            valign='middle', height=('relative', 95),
            min_width=20, min_height=9)
        urwid.MainLoop(self.top, palette=[('reversed', 'standout', '')], unhandled_input = self.exit_on_q).run()


if __name__ == '__main__':
    myBookHandler = BookHandler.BookHandler()
    books = myBookHandler.search('hackers')
    main = Menu(books)
    main.runLoop()

