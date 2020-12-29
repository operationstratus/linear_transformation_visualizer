import tkinter as tk
import math

S = 800
a = math.pi / 40

U = 40

BASE = [
     [1, 2],
     [2, 1]
    ]
print("BASE =")
for row in BASE:
    print(row)

B = [
     [0, -1],
     [2, 0]
    ]
print("B =")
for row in B:
    print(row)


def matrix_mult(A, B):
    C = []
    for row in A:
        C.append([row[0]*B[0][0] + row[1]*B[1][0] , row[0]*B[0][1] + row[1]*B[1][1] ])
    return C
A = matrix_mult(B, BASE)
print("A = ")
for row in A:
    print(row)


'''
A = [
     [math.cos(a)*2, -math.sin(a)],
     [math.sin(a), math.cos(a)]
    ]
'''
'''
A = [
     [1, 0],
     [0, 1]
    ]
'''

root = tk.Tk()
CANVAS = tk.Canvas(root, width=S, height=S, background="black")
CANVAS.pack(fill="both", expand=True)

#CANVAS.create_oval(-5,-5,5,5, fill="red")
CANVAS.configure(scrollregion=(-S/2, -S/2, S/2, S/2))
CANVAS.xview_moveto(.5)
CANVAS.yview_moveto(.5)


def X(x, y):
    return x*A[0][0]+y*A[0][1]
def Y(x, y):
    # OBS here are the solution to the problem with tkinter having positive y direction pointing downwards
    return -x*A[1][0]-y*A[1][1]

def create_coordinate_system():
    for i in range(int(-S/2), int(S/2), int(U)):
        if i == 0:
            w = 3
        else:
            w = 1
        mid = int(S/2)
        # ORIGINAL GRID
        CANVAS.create_line(mid, i, -mid, i, fill='gray', width=w) # x axis
        CANVAS.create_line(i, -mid, i, mid, fill='gray', width=w)
        # TRANSFORMED GRID
        CANVAS.create_line(X(-mid, i), Y(-mid, i), X(mid, i), Y(mid, i), fill='white', width=w) # x axis
        CANVAS.create_line(X(i, -mid), Y(i, -mid), X(i, mid), Y(i, mid), fill='white', width=w) # y axis

'''
def create_coordinate_system():
    mid = int(S/2)
    w = 1
    CANVAS.create_line(-mid, 0, mid, 0, fill='white', width=w)
    CANVAS.create_line(0, -mid, 0, mid, fill='white', width=w)
'''
def vec(x, y, color='yellow'):
    print("vec: " + str(X(x, y)) + ", " + str(X(x, y)) )
    x = x*U
    y = y*U
    CANVAS.create_line(0, 0, X(x, y), Y(x, y), fill=color, width=4)


def show_standard_base_vectors():
    vec(1, 0, 'green')
    vec(0, 1, 'red')

def rect(x1, y1, x2, y2, x3, y3, x4, y4):
    x1 = x1*U
    y1 = y1*U
    x2 = x2*U
    y2 = y2*U
    x3 = x3*U
    y3 = y3*U
    x4 = x4*U
    y4 = y4*U
    points = [X(x1, y1), Y(x1, y1), X(x2, y2), Y(x2, y2), X(x3, y3), Y(x3, y3), X(x4, y4), Y(x4, y4)]
    CANVAS.create_polygon(points, outline='#f11', fill='#1f1', width=2)
    
def vec_in_standard_base(x, y, color="blue"):
    x = x*U
    y = -y*U
    CANVAS.create_line(0, 0, x, y, fill=color, width=4)


# MAIN
create_coordinate_system()
show_standard_base_vectors()
vec(1, 1)
#rect(0, 0, 0, 1, 1, 1, 1, 0)
#vec(1, 0)
#vec_in_standard_base(1, 1)

root.mainloop()