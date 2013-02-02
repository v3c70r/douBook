import wx
import wx.html
import BookHandler

class SearchPanel(wx.Panel):        #search Panel
    def __init__(self, parent, *args, **kwargs):
        '''Create a book searching panel'''
        wx.Panel.__init__(self, parent, *args, **kwargs)
        self.__initUI()
    def __initUI(self):
        '''initialize UI'''
        self.searchText = wx.TextCtrl(self)             #Text
        staticBmp = wx.StaticBitmap(parent = self, bitmap = wx.Bitmap("./logo.bmp"))    #douban Logo

        searchBtn = wx.Button(self,  label = "search")  #Create a Button
        searchBtn.Bind(wx.EVT_BUTTON, self.DoSearch)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)             #Horizontal Box for searching text and button
        hsizer.Add(self.searchText, 0, wx.ALIGN_CENTER|wx.ALL,5)
        hsizer.Add(searchBtn, 0, wx.ALIGN_CENTER|wx.ALL,5)
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(staticBmp, 0, wx.ALIGN_CENTER|wx.ALL,5)
        vsizer.Add(hsizer, 0, wx.ALIGN_CENTER|wx.ALL,5)
        self.SetSizerAndFit(vsizer)



    def DoSearch(self, event = None):
        #Do search, virtual function, dialog to test
        '''Search books and show them in the grid'''
        dlg = wx.MessageDialog(self,
                               message= 'Virtual',
                               caption='Raiting',
                               style=wx.OK|wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()


        
class SearchByNamePanel(SearchPanel):          #ISBN Panel
    def __init(self, parent, *args, **kwargs):
        '''Create a book searching panel'''
        SearchPanel.__init__(self, parent, *args, **kwargs)
    def DoSearch(self, event = None):
        '''Search books and show them in the grid'''
        dlg = wx.MessageDialog(self,
                               message='Searching name '+self.searchText.GetValue(),
                               caption='Search by name',
                               style=wx.OK|wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()



class SearchByISBNPanel(SearchPanel):          #ISBN Panel
    def __init(self, parent, *args, **kwargs):
        '''Create a book searching panel'''
        SearchPanel.__init__(self, parent, *args, **kwargs)

    def DoSearch(self, event = None):
        '''Search books'''
        myBookHandler = BookHandler.BookHandler()
        myBook= myBookHandler.getBookById("id")
        dlg = wx.MessageDialog(self,
                               message = 'Title: '+myBook.getTitle()+
                               '\nSubtitle'+myBook.getSubtitle(),
                               caption = 'Message Box',
                               style=wx.OK|wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()



class HTMLPanel(wx.Panel):          #The HTML Panel that shows the details of the book
    def __init__(self, parent, *args, **kwargs):
        '''Create an HTML'''
        wx.Panel.__init__(self, parent, *args, **kwargs)
        self.__initUI()
    def __initUI(self):
        pass


class MainFrame(wx.Frame):          #The main frame that contains all panels
    '''Main frame'''
    def __init__(self, *args, **kwargs):
        '''Create the MainFrame'''
        wx.Frame.__init__(self, *args, **kwargs)

        #Creat a panel and put a notebook on it
        mainPanel = wx.Panel(self)
        noteBook = wx.Notebook(mainPanel)

        #Add the panels to notebook
        page1 = SearchByNamePanel(noteBook)
        page2 = SearchByISBNPanel(noteBook)

        #add a HTML to main panel
        htmlPanel = HTMLPanel(mainPanel, size=(700, 600))

        #Add Labels
        noteBook.AddPage(page1, "Search Book by Name")
        noteBook.AddPage(page2, "Search Book by ISBN")

        #Creat an sizer
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(noteBook, 1, wx.EXPAND)
        sizer.Add(htmlPanel, 1, wx.EXPAND)
        mainPanel.SetSizer(sizer)


#Main function, maybe necessary, maybe not
if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None, title = 'douban book', size = (800, 600))
    frame.Show()
    app.MainLoop()



