from tkinter import *
from tkinter import messagebox

def visualize(pattern_in, dim_x, dim_y, edit):
    window = Tk()
    if(edit == True):
        window.title("Pattern visualization - close to save changes")
    if(edit == False):
        window.title("Pattern visualization")
    square_size = 50
    size = str(dim_x * square_size) + "x" + str(dim_y * square_size)
    window.geometry(size)

    btns = [] 

    pattern = pattern_in
    
    def change(k):
        if(pattern[k]==1):
            pattern[k]=-1
            btns[k].configure(bg = "white", fg = "black")
        elif(pattern[k]==-1):
            pattern[k]=1
            btns[k].configure(bg = "black", fg = "white")
            
        #messagebox.showinfo(k,k)

    k=0
    for i in range(dim_y):
        for j in range(dim_x):
            number = str(k)
            if(pattern[k]==1):
                if(edit == True):
                    btn = Button(window, bg="black", fg="white", height="2", width="5", text=number, command=lambda m=k: change(m))
                    btns.append(btn)
                    btn.grid(row = i, column = j)
                if(edit == False):
                    lbl = Label(window, bg="black", fg="white", height="2", width="5", text=number)
                    lbl.grid(row = i, column = j)
            else:
                if(edit == True):
                    btn = Button(window, bg="white", height="2", width="5", text=number, command=lambda m=k: change(m))
                    btns.append(btn)
                    btn.grid(row = i, column = j)
                if(edit == False):
                    lbl = Label(window, bg="white", height="2", width="5", text=number)
                    lbl.grid(row = i, column = j)
            k=k+1


    window.mainloop()

    return pattern
