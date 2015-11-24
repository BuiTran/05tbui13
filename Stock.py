'''
Created on Nov 16, 2015

@author: TranBui
'''

class Stock(object):
    '''
    A Stock object that encapsulates the information of a single stock
    '''


    def __init__(self, date, op, hi, lo, cl, vol, adj_cl):
        '''
        Constructor
        '''
        self.date = date
        self.op = op
        self.hi = hi
        self.lo = lo
        self.cl = cl
        self.vol = vol
        self.adj_cl = adj_cl
        
        