'''
Created on Nov 15, 2015

@author: TranBui
'''
import urllib
from datetime import datetime
from Stock import Stock
class StockReader(object):
    
    '''
    fetches the data and creates/holds a collection of stock instances
    '''


    def __init__(self, symbol, start = None, end = None):
        '''
        Constructor
        '''
        self.symbol = symbol
        self.start = start
        self.end = end
        self.setUrl()
        data = urllib.urlopen(self.url).read()
        data = data.decode("utf-8")
        #split the data and put into the list. Also get rids of the top and bottom col
        rawstock_list = data.split('\n')[1:-1]
        self.sLow = 100000
        self.lHigh = 0
        #The list of stocks objects
        self.stock_list = []
        for stock in rawstock_list:
            stock_data = stock.split(",")
            date=datetime(*(map(int,stock_data[0].split('-'))))
            stock = Stock(date, float(stock_data[1]),float(stock_data[2]),float(stock_data[3]), float(stock_data[4]), int(stock_data[5]), float(stock_data[6]))
            self.stock_list.append(stock)
            if (self.sLow > stock.lo):
                self.sLow = stock.lo
            if (self.lHigh < stock.hi):
                self.lHigh = stock.hi
        
    def getSLow(self):
        return self.sLow
    
    def getLHigh(self):
        return self.lHigh
            
    def getEDate(self):
        return self.start
    
    def getLDate(self):
        return self.end
    
    def setUrl(self):
        '''Setup the url to the data'''
        #base url
        self.url = "http://ichart.finance.yahoo.com/table.csv?s="
        #add symbol (AAPL)
        self.url += self.symbol
        if self.start:
            self.url+="&a=%i&b=%i&c=%i"%(self.start.month-1,self.start.day,self.start.year)
        if self.end:
            self.url+="&d=%i&e=%i&f=%i"%(self.end.month-1,self.end.day,self.end.year)
        self.url+="&g=d"
        
        
        
    
    
        
        
        
       