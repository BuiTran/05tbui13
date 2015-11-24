'''
Created on Nov 23, 2015

@author: TranBui
'''
import matplotlib.pyplot as plt

from ViewPort import ViewPort
class MatplotCharting(object):
    '''
    Plotting the graph from the data using matplotlib
    '''


    def __init__(self, stockReader):
        '''
        Constructor
        '''
        x = [s.date for s in stockReader.stock_list]
        y = [s.op for s in stockReader.stock_list]
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
        plt.figure(num=None, figsize=(13, 6), dpi=80, facecolor='w', edgecolor='k')
        plt.plot(x,y)
       
        plt.title(str(stockReader.symbol) + "Stock Prices")
        plt.xlabel("Date")
        plt.ylabel("Open Prices")
        plt.show()
        
        print(x)
        print(y)
        
        
