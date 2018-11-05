from tkinter import *


def visualize(pattern, dim_x, dim_y, edit):
    window = Tk()
    window.title("Pattern visualization")
    square_size = 50
    size = str(dim_x * square_size) + "x" + str(dim_y * square_size)
    window.geometry(size)
    
    if(edit == False): #we only want to show pattern, not edit it
        k=0
        for i in range(dim_y):
            for j in range(dim_x):
                test = str(k)
                if(pattern[k]==1):
                    lbl = Label(window, bg="black", height="2", width="5", text=test)
                    lbl.grid(row = i, column = j)
                else:
                    lbl = Label(window, bg="white", height="2", width="5", text=test)
                    lbl.grid(row = i, column = j)
                k=k+1
    window.mainloop()
