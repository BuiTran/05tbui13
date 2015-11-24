'''
Created on Nov 15, 2015

@author: TranBui
'''
from tkinter import Frame,BOTH,Tk
import datetime
from ChartingCanvas import ChartingCanvas
from StockReader import StockReader
class MainFrame(Frame):
    '''
    presents our human interface in an TkInter image window
    '''


    def __init__(self, root, symbol, start, end):
        '''
        Constructor
        '''
        Frame.__init__(self, root, background="white")
        #Create the stock reader
        self.stockReader =StockReader(symbol, start, end)
        self.root = root
        #Create the canvas. We also pass in the stock reader (data) to the canvas 
        self.canvas = ChartingCanvas(root, self.stockReader)
        self.initUI()
    
    def initUI(self):
        self.root.title(self.canvas.chartTitle)
        self.pack(fill=BOTH, expand = 0)  
        
def main():
  
    root = Tk()
    root.geometry("700x700+300+0")
    d1 = datetime.datetime(2015, 1, 1)
    d2 = datetime.datetime.today()
    x = d2 - d1
    y = x / 10
    print((d1 + y).date())
    mainFrame = MainFrame(root,"AAPL", d1, d2)
    root.mainloop()  


if __name__ == '__main__':
    main()
        