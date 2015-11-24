'''
Created on Nov 14, 2015

@author: TranBui
'''

from tkinter import Frame,BOTH,Tk, Canvas
from ViewPort import ViewPort
from StockReader import StockReader
import datetime
class ChartingCanvas():
    '''
    paints the x-y plot (graph) based on the data
    '''


    def __init__(self, root, stockReader):
        '''
        Constructor
        '''
        self.canvas = Canvas(root)
        self.canvas.pack(side="top", fill="both", expand=True)
        self.init()
        #The size of the canvas is (vr - vl) = 500 x (vb - vt) = 500
        vl = 100
        vr = 600
        vt = 80
        vb = 580
        
        period = stockReader.getLDate() - stockReader.getEDate()
        #the x-coordinates of the world view is the number of days between the latest date and earliest date
        wl = 0
        wr = period.days
        #the y-coordinates of the world view is the range between the largest high and smallest low from stockReader
        wt = stockReader.getLHigh()
        wb = stockReader.getSLow()
        
        self.viewPort = ViewPort(wl, wr, wt, wb,
                                 vl, vr, vt, vb)
        
        self.initDraw(vl, vr, vt, vb, stockReader)
        
        self.drawGraph(stockReader)
        self.canvas.pack(fill=BOTH, expand=1)
        
        
        
        
        
    def initDraw(self, vl, vr, vt, vb, stockReader):
        period = stockReader.getLDate() - stockReader.getEDate()
        priceRange = stockReader.getLHigh() - stockReader.getSLow()
        #draw grid lines. 11 for each sides. Also set dates and prices for the grid
        for i in range(11):
            #Get the whole range for date and price
            dateText = (stockReader.getEDate() + i * period / 10).date()
            priceText = (stockReader.getLHigh() - i * priceRange / 10)
            #reformat to 2 decimal points
            p = float("{0:.2f}".format(priceText))
            #Drawing vertical grid and set text for each grid
            x = vl + i * self.verGrid
            self.drawVerticalLine(x, vt-10, (vb-vt)+20)
            self.canvas.create_text(x, vb+10, text = str(dateText), font=("Arial", 5))
            #Drawing horizontal grid and set text for each grid
            y = vt + i * self.horGrid
            self.drawHorizontalLine(vl-10, y, (vr - vl)+20)
            self.canvas.create_text(vl-25, y, text = str(p), font=("Arial", 5))
        #set the chart name
        self.canvas.create_text(700/2, 700 / 15, text = (str(stockReader.symbol) + " Stock Prices"), font=("Arial", 20))
        #set title for horizontal
        self.canvas.create_text(700/2, 700 - 50, text = "Dates", font=("Arial", 9))
        
            
    #Plot the graph based on the data from stock reader
    def drawGraph(self, stockReader):
        for stock in stockReader.stock_list:
            wx = (stock.date - stockReader.getEDate()).days
            wy = stock.op
            #Get vx, vy from wx, wy based on viewPort
            vx, vy = self.viewPort.toPixels(wx, wy)
            #Draw the point on the graph
            x1, y1 = ( vx - 1 ), ( vy - 1 )
            x2, y2 = ( vx + 1 ), ( vy + 1 )
            self.canvas.create_oval( x1, y1, x2, y2, fill = "#A8FDA0" )

        
    def init(self):
        self.verGrid = 50
        self.horGrid = 50
        self.chartTitle = "Stock Graph"
        self.horTitle = ""
        self.verTitle = ""
    
    #Getters and setters
    def getVerGrid(self):
        return self.verGrid
    
    def setVerGrid(self, verGrid):
        self.verGrid = verGrid
    
    def getHorGrid(self):
        return self.horGrid
    
    def setHorGrid(self,horGrid):
        self.horGrid = horGrid
        
    def getVerTitle(self):
        return self.verTitle
    
    def setVerTitle(self, verTitle):
        self.verTitle = verTitle
        
    def getHorTitle(self):
        return self.horTitle
    
    def setHorTitle(self, horTitle):
        self.horTitle = horTitle
        
    def getChartTitle(self):
        return self.chartTitle
    
    def setChartTitle(self, chartTitle):
        self.chartTitle = chartTitle
        
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def drawVerticalLine(self,x1,y1,length):
        self.canvas.create_line(x1,y1,x1,y1+length)
    
    def drawHorizontalLine(self,x1,y1,length):
        self.canvas.create_line(x1,y1,x1+length,y1) 
    
        
    
