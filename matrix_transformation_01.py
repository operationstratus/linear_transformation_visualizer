import tkinter as tk
import math


# GLOBAL CONSTANTS
S = 800
U = 40

ROOT = tk.Tk()
CANVAS = tk.Canvas(ROOT, width=S, height=S, background="black")
CANVAS.pack(fill="both", expand=True)
CANVAS.configure(scrollregion=(-S/2, -S/2, S/2, S/2))
CANVAS.xview_moveto(.5)
CANVAS.yview_moveto(.5)

I = [
     [1, 0],
     [0, 1]
    ]

class Base_system():
    def __init__(self, base=I, trans_matrix=I):
        self.__base = base
        self.__trans_matrix = trans_matrix
        self.__m_tot = matrix_mult(self.__base, self.__trans_matrix)
            # WHAT?? It seems that I have to calculate the total matrix as base matrix * transformation matrix and not the other way around
        self.__standard = self.__base == I
    
    def X_base(self, x, y):
        return x*self.__base[0][0]+y*self.__base[0][1]
    def Y_base(self, x, y):
        # OBS here are the solution to the problem with tkinter having positive y direction pointing downwards
        return -x*self.__base[1][0]-y*self.__base[1][1]
    
    def X(self, x, y):
        return x*self.__m_tot[0][0]+y*self.__m_tot[0][1]
    def Y(self, x, y):
        # OBS here are the solution to the problem with tkinter having positive y direction pointing downwards
        return -x*self.__m_tot[1][0]-y*self.__m_tot[1][1]
    
    def vec_base(self, x, y, color='yellow'):
        x = x*U
        y = y*U
        CANVAS.create_line(0, 0, self.X_base(x, y), self.Y_base(x, y), fill=color, width=4)
    
    def vec(self, x, y, color='yellow'):
        x = x*U
        y = y*U
        CANVAS.create_line(0, 0, self.X(x, y), self.Y(x, y), fill=color, width=4)
    
    def rect(self, x1, y1, x2, y2, x3, y3, x4, y4):
        x1 = x1*U
        y1 = y1*U
        x2 = x2*U
        y2 = y2*U
        x3 = x3*U
        y3 = y3*U
        x4 = x4*U
        y4 = y4*U
        points = [self.X(x1, y1), self.Y(x1, y1), self.X(x2, y2), self.Y(x2, y2), self.X(x3, y3), self.Y(x3, y3), self.X(x4, y4), self.Y(x4, y4)]
        CANVAS.create_polygon(points, outline='#f11', fill='#1f1', width=2)
    
    def base_coordinate_system(self):
        for i in range(int(-S/2), int(S/2), int(U)):
            if i == 0:
                w = 3
            else:
                w = 1
            mid = int(S/2)
            
            CANVAS.create_line(self.X_base(-mid, i), self.Y_base(-mid, i), self.X_base(mid, i), self.Y_base(mid, i), fill='gray', width=w) # x axis
            CANVAS.create_line(self.X_base(i, -mid), self.Y_base(i, -mid), self.X_base(i, mid), self.Y_base(i, mid), fill='gray', width=w) # y axis
            self.vec_base(1, 0, 'green')
            self.vec_base(0, 1, 'red')
    
    def transformed_coordinate_system(self):
        if self.__standard:
            colour = 'gray'
        else:
            colour = 'white'
        for i in range(int(-S/2), int(S/2), int(U)):
            if i == 0:
                w = 3
            else:
                w = 1
            mid = int(S/2)
            CANVAS.create_line(self.X(-mid, i), self.Y(-mid, i), self.X(mid, i), self.Y(mid, i), fill=colour, width=w) # x axis
            CANVAS.create_line(self.X(i, -mid), self.Y(i, -mid), self.X(i, mid), self.Y(i, mid), fill=colour, width=w) # y axis
        # base vectors
        self.vec(1, 0, 'green')
        self.vec(0, 1, 'red')



def matrix_mult(a, b):
    c = []
    for row in a:
        c.append([row[0]*b[0][0] + row[1]*b[1][0] , row[0]*b[0][1] + row[1]*b[1][1] ])
    return c



# MAIN
standard = Base_system()
standard.base_coordinate_system()


beta = Base_system([
     [1, 2],
     [2, 1]
    ], [
     [0, -1],
     [2, 0]
        ])
beta.base_coordinate_system()
beta.vec(1,1)


ROOT.mainloop()