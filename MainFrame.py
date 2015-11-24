'''
Created on Nov 15, 2015

@author: TranBui
'''
from Tkinter import Frame,BOTH,Tk
import datetime
from ChartingCanvas import ChartingCanvas
from StockReader import StockReader
from MatplotCharting import MatplotCharting
class MainFrame(Frame):
    '''
    presents our human interface in an TkInter image window
    The size for the frame is 700x700
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
 
    mainFrame = MainFrame(root,"AAPL", d1, d2)
     
    #Plotting with matplot
    
    stockReader =StockReader("AAPL", d1, d2)
    matplotCharting = MatplotCharting(stockReader)
    
    root.mainloop()  


if __name__ == '__main__':
    main()
        