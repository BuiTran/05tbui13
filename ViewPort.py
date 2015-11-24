'''
Created on Nov 17, 2015

@author: TranBui
'''

class ViewPort():
    '''
    A convenient helper object that helps convert world data converted to pixel 
    coordinates
    '''


    def __init__(self, wl, wr,wt,wb, vl, vr, vt, vb):
        '''
        Constructor
        '''
        self.wl = wl
        self.wr = wr
        self.wt = wt
        self.wb = wb
        self.vl = vl
        self.vr = vr
        self.vt = vt
        self.vb = vb
    
    #Convert wx wy to vx vy based on the formula in the instruction
    def toPixels(self, wx, wy):
        vx = self.vl + (self.vr-self.vl)*(wx-self.wl)/(self.wr - self.wl)
        vy = self.vb + (self.vt-self.vb)*(wy-self.wb)/(self.wt-self.wb)
        return (vx,vy)
        